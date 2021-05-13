
N,K = map(int, input().split())

c = 1
ans = K

for i in range(N-1):
    c = c*(K-1)

print(ans*c)