L = sorted(list(map(int, input().split())))
K = int(input())
ans = L[0] + L[1] + L[2]*(2**K)
print(ans)