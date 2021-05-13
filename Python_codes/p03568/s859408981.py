import sys

input = sys.stdin.readline
MOD = 1000000007

N = int(input())

A = list(map(int,input().split()))

odd = 0
for i in range(len(A)):
    if A[i]%2 == 0:
        odd += 1

print(3**len(A)-2**odd)