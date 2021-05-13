n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
a_sum = 0
b_sum = 0
for i in range(n):
    c.append(b[i]-a[i])
    if c[i] < 0:
        b_sum += c[i]
    else:
        a_sum += c[i]//2

if a_sum < abs(b_sum):
    print("No")
else:
    print("Yes")