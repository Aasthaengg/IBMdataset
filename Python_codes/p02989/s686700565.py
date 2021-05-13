n=int(input())
D=list(map(int,input().split()))
D=sorted(D,reverse=True)
print(D[n//2-1]-D[n//2])