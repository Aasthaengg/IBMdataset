N=int(input())
ans=next([x,y,N*x*y//(4*x*y-N*(x+y))]for x in range(1,3501)for y in range(1,3501)if 4*x*y>N*(x+y) and (N*x*y)%(4*x*y-N*(x+y))==0)
print(*ans)