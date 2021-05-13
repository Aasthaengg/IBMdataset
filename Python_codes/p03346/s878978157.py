# AGC024B


n = int(input())
a = [None] * n
for i in range(n):
    num = int(input())
    a[i] = num-1

seen = [False] * n
counts =[1] * n
for num in a:
    seen[num] = True
    if num>=1 and seen[num-1]:
        counts[num] = counts[num-1] + 1
print(n - max(counts))