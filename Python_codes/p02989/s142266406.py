n=int(input())
D=sorted(list(map(int,input().split())))
print(D[n//2]-D[(n-1)//2])