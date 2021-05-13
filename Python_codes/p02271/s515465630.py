#coding:utf-8
#1_5_A
from itertools import combinations

n = int(input())
A = list(map(int, input().split()))
q = int(input())
ms = list(map(int, input().split()))

numbers = set()
for i in range(1, n+1):
    for com in combinations(A, i):
        numbers.add(sum(com))

for m in ms:
    if m in numbers:
        print("yes")
    else:
        print("no")