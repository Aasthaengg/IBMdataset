a,b = map(int, input().split())
A1=int((a//0.08)//1)
A2=int((a+2//0.08)//1)
B1=b*10
B2=(b+2)*10
s=min(A1,A2,B1,B2)
t=max(A1,A2,B1,B2)
ans=-1
for i in range(s,t+1):
    if i*0.08//1==a and i*0.1//1==b:
        ans=i
        break
print(ans)