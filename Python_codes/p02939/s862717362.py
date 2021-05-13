import sys
def S(): return sys.stdin.readline().rstrip()
S = S()
ans = 1
compared = S[0]
now = ''
for x in S[1:]:
    now += x
    if compared!=now:
        ans +=1
        compared = now
        now = ''
print(ans)
