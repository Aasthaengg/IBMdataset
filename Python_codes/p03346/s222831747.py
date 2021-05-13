n = int(input())
P = list(int(input()) for _ in range(n))
tmp = [0]*(n+1)
for p in P:
    tmp[p] = tmp[p-1] + 1
print(n-max(tmp))