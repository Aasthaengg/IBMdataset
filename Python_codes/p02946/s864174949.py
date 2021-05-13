k,x=map(int,input().split())
ans1=x-k+1
ans2=x+k
ans3=[x for x in range(ans1,ans2)]
print(*ans3) 
