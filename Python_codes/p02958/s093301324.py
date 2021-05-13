N=int(input())
p=list(map(int,input().split()))

k=0
for i in range(N):
    if i+1!=p[i]:
        if k>2:
            break
        k+=1

print('YNEOS'[k>2::2])
