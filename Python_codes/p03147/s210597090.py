N = int(input())
H = list(map(int,input().split()))
print(sum(max(0,H[n]-H[n+1]) for n in range(N-1))+H[-1])