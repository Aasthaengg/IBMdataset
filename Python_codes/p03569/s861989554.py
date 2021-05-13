S=input()
xs=S.split('x')
xs=''.join(xs)

if xs!=xs[::-1]:
    print(-1)
else:
    ans=0
    N=len(S)
    M=len(xs)
    count1=[0]*(M+1)
    count2=[0]*(M+1)
    rs=S[::-1]
    i=j=0
    a=b=0
    while i<N:
        if S[i]!='x':
            a+=1
        else:
            count1[a]+=1
        if rs[i]!='x':
            b+=1
        else:
            count2[b]+=1
        i+=1
    for a,b in zip(count1,count2):
        ans+=abs(a-b)
    print(ans//2)