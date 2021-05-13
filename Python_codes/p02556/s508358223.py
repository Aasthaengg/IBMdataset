N = int(input())
A = []
B = []
for i in range(N):
    x, y = map(int, input().split())
    A.append(x+y)
    B.append(x-y)
print(max(max(A)-min(A), max(B)-min(B)))