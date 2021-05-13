n,m=map(int,input().split())
s=input()

ans=[]
s=s[::-1]

now=0
while now<n:
    for i in range(m,0,-1):
        if now+i<=n and s[now+i]=="0":
            ans.append(i)
            now=now+i
            break
    else:
        print(-1)
        break
else:
    ans=[str(i) for i in ans]
    print(" ".join(ans[::-1]))
