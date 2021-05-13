H,W=map(int,input().split())
s0='.'*(W+2)
s1='.'+input()+'.'

ans=''
for i in range(H):
    if i==H-1:
        s2='.'*(W+2)
    else:
        s2='.'+input()+'.'
    
    for j in range(1,W+1):
        if s1[j]=='.':
            x=s0[j-1:j+2]+s1[j-1]+s1[j+1]+s2[j-1:j+2]
            ans+=str(x.count('#'))
        else:
            ans+='#'
    s0=s1
    s1=s2

for i in range(H):
    print(ans[i*W:i*W+W])