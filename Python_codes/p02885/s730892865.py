# coding: utf-8

(a,b) = map(int, input().rstrip().split(" "))

ans = max(0, a-(b*2))

print(ans)