l = list(input())
n = len(l)

seg = []
for i in range(n-1):
    if l[i] != l[i+1]:
        seg.append(i)
print(len(seg))
