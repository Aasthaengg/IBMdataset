n = int(input())

for i in range(1, 1000+1):
    if n == i*(i-1)//2:
        k = i
        break
else:
    print("No")
    exit()

s = [[] for _ in range(k+1)]
num = 0
for i in range(1, k):
    for j in range(i):
        num += 1
        s[i].append(num)
        if j == i-1:
            s[k].append(num)
        else:
            s[j+1].append(num)
print("Yes")
print(k)
for i in range(1, k+1):
    print(k-1, *s[i])
