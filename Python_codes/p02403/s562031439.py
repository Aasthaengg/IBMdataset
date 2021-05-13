ans=[]

while True:
    H,W=map(int,input().split())
    if W==H==0:
        break
    ans.append(('#'*W+'\n')*H)

print('\n'.join(ans))
