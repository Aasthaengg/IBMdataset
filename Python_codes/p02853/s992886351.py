# coding: utf-8

(x,y) = map(int, input().rstrip().split(" "))

ans = sum([max(0, 400000 - (i * 100000)) for i in [x,y]])
if x == 1 and y == 1:
    ans += 400000
print(ans)