N = int(input())
D = sorted(map(int,input().split()))
print(max(0,D[N//2]-D[N//2-1]))