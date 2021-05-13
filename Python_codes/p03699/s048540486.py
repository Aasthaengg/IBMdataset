n = int(input())
s = [int(input()) for _ in range(n)]

s.sort()

point = sum(s)

if point%10 == 0:
    for i in s:
        if i%10 != 0:
            point -= i
            break

if point%10 == 0:
    print(0)
else:
    print(point)