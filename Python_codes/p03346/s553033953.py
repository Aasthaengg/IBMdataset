n = int(input())
p = []
l = [0]*n
count = 0
for i in range(n):
    count = count + 1
    p1 = int(input())
    p.append(p1)
    l[p1-1] = count
count1 = 1
l2 = [1]
for i in range(n-1):
    if l[i] <  l[i+1]:
        count1 = count1 + 1
        l2.append(count1)
    else:
        count1 = 1
print(n-max(l2))