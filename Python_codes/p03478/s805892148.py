# coding: utf-8

S = input().split()

N = int(S[0])
A = int(S[1])
B = int(S[2])

total = 0

for i in range(1, N+1):
    j = i
    dig = 0
    while i > 0:
        dig += i % 10
        i = int(i / 10)
    if dig >= A and dig <= B:
        total += j

print(total)
