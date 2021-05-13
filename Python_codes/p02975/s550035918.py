n = int(input())
a = [int(x) for x in input().split()]

res = a[0]
for i in range(1,n):
    res = res^a[i]
if res == 0:
    print("Yes")
else:
    print("No")