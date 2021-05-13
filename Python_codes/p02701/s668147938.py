N = int(input())
preans = []
for _ in range(N):
    n = input()
    preans.append(n)
ans = set(preans)
print(len(ans))