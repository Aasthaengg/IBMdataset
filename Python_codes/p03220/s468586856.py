N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
min = 0
for i in range(N):
    if abs(T - H[min] * 0.006 - A) > abs(T - H[i] * 0.006 - A):
        min = i
print(min+1)
