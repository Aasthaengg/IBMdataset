
n = int(input())
k = int(input())
a = [1]

for i in range(n):
    if a[i] <= k:
        a.append(a[i] *2)
    else:
        a.append(a[i] + k)
#print(a)
print(a[-1])
