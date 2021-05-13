
n = int(input())
bott = 0
rem = -1
for i in range(10000):
    bott = i*(i+1)//2
    bott2 = (i+1)*(i+2)//2
    if(bott<=n and n<bott2):
        rem = bott2-n
        bott = i
        break
ans = []
for i in range(bott+1):
    if(i+1 != rem):
        ans.append(i+1)

for i in ans:
    print(i)
