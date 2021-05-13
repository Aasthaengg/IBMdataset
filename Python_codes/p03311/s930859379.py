n = int(input())
a = [int(j)-int(i)-1 for i, j in enumerate(input().split())]
a.sort()
num = n/2
if num.is_integer():
    num = num-1
val = a[int(num)]
ans = sum([abs(i-val) for i in a])
print(ans)
