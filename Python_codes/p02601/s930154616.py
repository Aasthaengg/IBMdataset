a, b, c = map(int, input().split())
k = int(input())

cnt = 0
while True:
    if a < b:
        break
    cnt += 1
    b *= 2

while True:
    if b < c:
        break
    cnt += 1
    c *= 2

if cnt > k:
    print("No")
else:
    print("Yes")