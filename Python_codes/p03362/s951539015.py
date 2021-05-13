n = int(input())

num = [1]*55556

for i in range(2,55556):
    if num[i]==1:
        k=2
        while i*k<=55555:
            num[i*k]=0
            k+=1

ans = []

l=2
for i in range(n):
    for j in range(l,11111):
        if num[j*5+1]==1:
            ans.append(str(j*5+1))
            l=j+1
            break
print(' '.join(ans))
