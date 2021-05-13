n=int(input())
d=list(map(int,input().split()))
ans=0
di=sorted(d)
half1=di[(n-1)//2]
half2=di[(n-1)//2+1]
ans=half2-half1
print(ans)