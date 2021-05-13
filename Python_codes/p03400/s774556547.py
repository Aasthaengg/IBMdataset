N = int(input())
D, X = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))

ans = 0
for a in A:
    if D%a == 0:
        ans += D // a
    else:
        ans += D//a + 1

print(ans+X)