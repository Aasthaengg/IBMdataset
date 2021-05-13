a, b, c = map(int, input().split())
k = int(input())
cnt = 0
while a >= b:
    b = b * 2
    cnt += 1
while b >= c:
    c = c * 2
    cnt += 1
if k >= cnt:
    print("Yes")
else:
    print("No")