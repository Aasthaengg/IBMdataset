n = int(input())
l = list(map(int, input().split()))
l1 = [0]*n
l1[1] = abs(l[0] - l[1])
for i in range(2, n):
    l1[i] = min(l1[i - 2] + abs(l[i] - l[i - 2]), l1[i - 1] + abs(l[i] - l[i - 1]))
print(l1[n - 1])