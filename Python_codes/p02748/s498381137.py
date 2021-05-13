# coding: utf-8
# Your code here!

A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
coupon = [list(map(int, input().split())) for _ in range(M)]
a_min, b_min = min(a), min(b)
discount = []
for i in range(M):
    discount.append(a[coupon[i][0] - 1] + b[coupon[i][1] - 1] - coupon[i][2])
if a_min + b_min < min(discount):
    print(a_min + b_min)
else:
    print(min(discount))