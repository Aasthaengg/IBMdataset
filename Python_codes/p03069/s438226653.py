import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
s = input()
v1 = [None]*n
v2 = [None]*n
v = 0
for i in range(n):
    if s[i]=="#":
        v += 1
    v1[i] = v
v1.insert(0,0)
v = 0
for i in range(n-1, -1, -1):
    if s[i]==".":
        v += 1
    v2[i] = v
v2.append(0)
ans = min((v1[i]+v2[i]) for i in range(n+1))
print(ans)