import itertools,sys
def I(): return int(sys.stdin.readline().rstrip())
def S(): return sys.stdin.readline().rstrip()
N = I()
s,t = S(),S()
ans = len(s)+len(t)
t_accumulate = list(itertools.accumulate(t))
for x in t_accumulate[::-1]:
    if x in s:
        ans -= len(x)
        break
print(ans)
