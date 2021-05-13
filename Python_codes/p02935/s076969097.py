n = int(input())
vn =list(map(int, input().split()))

vn.sort()

a = (vn[0]+vn[1])*0.5

for i in range(2, n):
    a = (a+vn[i])*0.5


print(a)
