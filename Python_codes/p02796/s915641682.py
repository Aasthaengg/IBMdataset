n=int(input())
st=[]
for i in range(n):
    x,l=map(int,input().split())
    st.append([x-l,x+l])
st.sort(key=lambda x:x[1])
now,ans=0,0
while now<n:
    t=st[now][1]
    while True:
        now+=1
        if now==n: break
        if st[now][0]>=t: break
    ans+=1
print(ans)