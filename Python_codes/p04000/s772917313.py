from collections import defaultdict
d = defaultdict(int)

h,w,n = map(int, input().split())
a = [0]*n
b = [0]*n
for i in range(n):
    a[i],b[i] = map(int, input().split())
    a[i] -= 1; b[i] -= 1
    
## 左上のマスを(0,0)とする
## 正方形の左上のマスを(j,i)とする

for x in range(n):
    for k in range(3):
        for l in range(3):
            i = a[x]-k ; j = b[x]-l
            if i<0 or i+3>h or j<0 or j+3>w:
                continue
            d[(j,i)] += 1

ans =[0]*10
for k,v in d.items():
    ans[v] += 1
ans[0] = (h-2)*(w-2)-sum(ans)

for i in range(10):
    print(ans[i])
