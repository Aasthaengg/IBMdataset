"""agc026_a"""
N = int(input())
A = list(map(int, input().split()))

ANS = 0
CNT = 0
LAST = 0

for a in A:
    if a == LAST:
        CNT += 1
        LAST = 0
    else: 
        LAST = a

print(CNT)