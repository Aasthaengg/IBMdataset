N = int(input())
D = sorted(map(int, input().split()))
print(0 if D[N//2]==D[N//2-1] else D[N//2]-D[N//2-1])