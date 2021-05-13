import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
L = [0]
for i in range(N):
    L.append(L[i]+A[i])
TotalLen = L[-1]
Center = TotalLen/2

temp = TotalLen
left = 0
right = 0
for i in range(N + 1):
    if abs(L[i] - Center) < temp:
        temp = abs(L[i] - Center)
        left = L[i]
        right = TotalLen - left
print(abs(left - right))
