N = int(input())
tpr, xpr, ypr = 0, 0, 0
count = 0
for i in range(N):
    t, x, y = map(int, input().split())
    d = abs(x-xpr) + abs(y-ypr)
    n = ((t-tpr) - d) / 2
    if n >= 0 and n % 1 == 0:
        count += 1
    tpr, xpr, ypr = t, x, y
if count == N:
    print("Yes")
else:
    print("No") 