N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
needed_minus = 0
for i in range(N):
    if a[i] > b[i]:
        needed_minus += a[i] - b[i]
    elif a[i] % 2 != b[i] % 2:
        needed_minus += 1
if needed_minus > sum(b) - sum(a):
    print("No")
else:
    print("Yes")