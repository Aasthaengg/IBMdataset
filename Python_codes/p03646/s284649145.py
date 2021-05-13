K = int(input())
N = 50
L = [i+K//N+(K%N+i>=N) for i in range(N)]
print(N)
print(*L)
