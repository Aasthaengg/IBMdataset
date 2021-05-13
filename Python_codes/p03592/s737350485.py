# B fLIP
n,m,k=map(int,input().split())

for h in range(n+1):
    for w in range(m+1):
        black=m*h+n*w-2*h*w
        if black==k:
            print('Yes')
            exit()
print('No')