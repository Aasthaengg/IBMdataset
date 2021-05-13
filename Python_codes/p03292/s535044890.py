ar = [int(i) for i in input().strip().split(" ")]
ar.sort()
s = 0
for i in range(1, len(ar)):
    s += (ar[i] - ar[i - 1])
print(s)