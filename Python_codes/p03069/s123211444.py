n=int(input())
c=str(input())
#c=c[::-1]
#print(c)
black=c.count('#')
white=n-black
left=0#左は黒を消す
right=white#右はしろを消す
#print(white,black)
ans=right
for i in range(n):
    if c[i]=='#':
        left+=1
    else:
        right-=1
    
    ans=min(ans,left+right)
print(ans)