n = int(input())
l = list(map(int,input().split()))
count = 0
for i in range(n):
    for ii in range(n):
        for iii in range(n):
            if l[i] + l[ii] > l[iii] and l[ii] + l[iii] > l[i] and l[iii] + l[i] > l[ii] and i<ii and ii < iii and l[i] != l[ii] and l[i] != l[iii] and l[ii] != l[iii]:
                count += 1
print(count)