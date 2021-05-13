a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
flg = abs(a - b) + w * t <= v * t
print(["NO", "YES"][flg])