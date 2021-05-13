s=input()
n=len(s)-1
ans=0

for bit in range(0, 1<<n):
    st=s
    for i in range(n+1):
        if (bit>>i)%2==0:
            continue
        st=st[:n-i]+'+'+st[n-i:]

    ans+=sum(list(map(int,st.split('+'))))
print(ans)
        
