n,m,k=map(int,input().split())
for a in range(n+1):
    for b in range(m+1):
        if b*n+a*m-2*a*b==k:
            print('Yes')
            break
    else:
        continue
    break
else:
    print('No')