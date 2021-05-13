N = int(input())
D = list(map(int, input().split()))
D = sorted(D)

print(D[N//2]-D[N//2-1])

