N=int(input())
S=input()
ans=[]
black=0
white=0
for n in range(N):
    if S[n]=='.':
        white+=1
    else:
        black+=1
stones={'b':0,'w':white}
for n in range(N):
    if S[n]=='#':
        stones['b']+=1
    else:
        stones['w']-=1
    ans.append(stones['b']+stones['w'])
if 'b' in stones:
    if stones['b']==N:
        print(0)
    else:
        print(min(min(ans),white,black))
else:
    print(min(min(ans),white,black))
