n,r=int(input()),-1
a = [int(input()) for _i in range(n)]+[-1]
for i in range(n):
    if a[i-1] >= a[i]:r+=a[i]
    elif a[i-1]+1==a[i]:r+=1
    else:r=-1;break
print(r)