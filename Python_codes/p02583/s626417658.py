n = int(input())
l = sorted(list(map(int, input().split())))

a = 0
        
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if l[k] < l[i] + l[j] and l[i] < l[j] and l[j] < l[k]:
                a += 1

print(a)
