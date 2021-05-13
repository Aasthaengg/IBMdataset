n = int(input())
L = list(map(int,input().split()))
L.sort()

from itertools import accumulate
li = list(accumulate(L))

cnt = 0
flag = False
for i in range(n-1):
    if li[i]*2 >= L[i+1]:
        flag =True
        cnt +=1
    else:
        flag =False
        cnt = 0
print(cnt+1)
