import sys
n = int(input())
ls = list(map(int,input().split()))
m = int(input())
di = list(map(int,input().split()))
dic = {}
for i in range(n):
    if dic.get(ls[i],0) == 0:
        dic[ls[i]] = 1
    else:
        dic[ls[i]] += 1
for k in range(m):
    if dic.get(di[k],0) == 0:
        print("NO")
        sys.exit()
    else:
        dic[di[k]] -= 1
print("YES")