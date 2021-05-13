N=int(input())
D=list(map(int,input().split()))
D.sort()
n=N//2
print(D[n]-D[n-1])