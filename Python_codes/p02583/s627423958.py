n = int(input())
l = [int(i) for i in input().split()]
l.sort()
count = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1,n):
            l1 = l[i]
            l2 = l[j]
            l3 = l[k]
            if (l1 != l2) &(l2 != l3)&(l1 + l2 > l3):
                count += 1
print(count)