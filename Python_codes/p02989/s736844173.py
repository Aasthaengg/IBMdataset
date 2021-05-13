N = int(input())
D = sorted(map(int, input().split()))
ans = D[N//2] - D[N//2-1]
print(ans)