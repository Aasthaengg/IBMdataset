k,x=map(int,input().split())
ans=[]
for i in range(x-(k*2-1)//2,x+(k*2)//2):
    ans.append(str(i))
print(" ".join(ans))