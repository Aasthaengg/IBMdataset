import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


x = input()
s = []
for c in x:
    if c=="T" and s and s[-1]=="S":
        s.pop()
    else:
        s.append(c)
ans = len(s)
print(ans)