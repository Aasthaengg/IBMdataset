N = int(input())
D, X = map(int,input().split())
A = []
for n in range(N):
    A.append(int(input()))

ans = N + X

D -= 1
for a in A:
    ans += D//a
print(ans)