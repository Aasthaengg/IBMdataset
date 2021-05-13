# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
answer = N
# 6円で払う部分と9円で払う部分を分ける
for i in range(N+1):
    temp = 0
    six_pay = i
    while six_pay:
        temp += six_pay%6
        six_pay //= 6
    nine_pay = N - i
    while nine_pay:
        temp += nine_pay%9
        nine_pay //= 9
    if temp < answer:
        answer = temp

print(answer)
