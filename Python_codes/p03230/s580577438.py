n = int(input())
k = 1
t = 0
while t < n:
    t += k
    k += 1

if t != n:
    print("No")
    exit(0)

print("Yes")
print(k)

a = [[] for _ in range(k)]
val = 1
for i in range(k-1):
    for j in range(i+1,k):
        a[i].append(val)
        a[j].append(val)
        val += 1

for aa in a:
    print(*([len(aa)] + aa))



