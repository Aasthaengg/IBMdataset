n = int(input())
ans = 0
s = 0
for i in range(1,n+1):
    if i*(i+1)//2 >= n:
        break
k = i*(i+1)//2 - n
for j in range(1,i+1):
    if j == k:
        pass
    else:
        print(j)