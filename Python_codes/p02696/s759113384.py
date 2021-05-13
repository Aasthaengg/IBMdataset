A, B, N = map(int, input().split())


x=min(B-1,N)
ans=((A*x)/B)//1 - A*((x/B)//1)
print(int(ans))

