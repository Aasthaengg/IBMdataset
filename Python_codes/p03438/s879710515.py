n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
A = 0
B = 0
for i in range(n):
    A += max(0, (b[i] - a[i]) // 2)
    B += max(0, a[i] - b[i])
if sum(b) >= sum(a):
    if A >= B:
        print("Yes")
        exit()
print("No")