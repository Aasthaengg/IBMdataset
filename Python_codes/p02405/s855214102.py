ans=[]

while True:
    H,W=map(int,input().split())
    if W==H==0:
        break
    b=''
    for i in range(H):
        for j in range(W):
            if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                b+='#'
            else:
                b+='.'
        b+='\n'
    ans.append(b)


print('\n'.join(ans))
