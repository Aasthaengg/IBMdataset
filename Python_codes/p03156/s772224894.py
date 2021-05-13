N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))

low, middle, high = 0, 0, 0
for i in range(N):
    if P[i] <= A:
        low += 1
    elif P[i] <= B:
        middle += 1
    else:
        high += 1
print(min(low, middle, high))
