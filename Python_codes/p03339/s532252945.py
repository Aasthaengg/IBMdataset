
N = int(input())
S = list(input()) #１文字ずつ
#print('S',S)

hidari, migi = 0,0
for i in range(1,N):
    if S[i]=='E':
        migi+=1

#print('count:',hidari,migi)
out=hidari+migi
#print('out0:', out)
ld=1  #leader

while ld<N:
    if S[ld-1]=='W' and S[ld]=='E':
        hidari+=1
        migi-=1
    elif S[ld-1]=='W' and S[ld]=='W':
        hidari+=1
    elif S[ld-1]=='E' and S[ld]=='E':
        #print('kokoda!')
        migi-=1
    #print('ld,hidari,migi,out:',ld,hidari,migi,migi+hidari)
    out = min(out,hidari+migi)
    ld+=1

print(out)