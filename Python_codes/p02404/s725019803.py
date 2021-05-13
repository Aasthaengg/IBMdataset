ans=[]

while True:
    H,W=map(int,input().split())
    if W==H==0:
        break
    r=''
    r+='#'*W+'\n'

    for i in range(H-2):
        r+='#'+'.'*(W-2)+'#\n'

    r+='#'*W+'\n'
    ans.append(r)

print('\n'.join(ans))
