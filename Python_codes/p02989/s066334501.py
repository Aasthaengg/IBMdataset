N=int(input())
*D,=map(int,input().split())
D.sort()
print((D[N//2]-D[N//2-1])*(N%2==0))