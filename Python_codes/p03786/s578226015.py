import itertools
n = int(input())
c = list(map(int,input().split()))
c.sort()
ac = list(itertools.accumulate(c))
check = [1]*n
for i in range(n-1):
    if ac[i]*2<c[i+1]:
        check[i] = -1
    else:
        check[i] = 1
tmp=0
for i in range(n):
    if check[i]==1:
        tmp+=1
    else:
        tmp =0
print(tmp)