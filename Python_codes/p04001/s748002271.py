s=input()
# ss=int(s)
n=len(s)
ans=int(s)
for bit in range(1<<(n-1)):
    if bit==0 : continue
    now=[] #+の位置
    for i in range(n):
        if bit>>i &1 :
            now.append(i)

    for i in range(len(now)-1):
        ans+=int(s[now[i]+1:now[i+1]+1])
    ans+=int(s[:now[0]+1])
    ans+=int(s[now[-1]+1:])

print(ans)