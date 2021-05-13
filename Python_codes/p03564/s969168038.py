from sys import stdin

n = int(stdin.readline().rstrip())
k = int(stdin.readline().rstrip())

ans = 1
for i in range(n):
    if ans*2 < ans+k:
        ans*=2
    else:
        ans+=k
print(ans)