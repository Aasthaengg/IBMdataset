n=int(input())
s1=input()
s2=input()
ans=0
i=0
prev=None#左のドミノの状態
if s1[0]==s2[0]:#縦
    ans=3
    i+=1
    prev='tate'
else:#横
    ans=6
    i+=2
    prev='yoko'
    
mod=10**9+7
while i<n:
    if s1[i]==s2[i]:#縦
        ans=(ans*2)%mod if prev=='tate' else ans 
        i+=1
        prev='tate'
    else:#横
        ans=(ans*2)%mod if prev=='tate' else (ans*3)%mod 
        i+=2
        prev='yoko'
print(ans)