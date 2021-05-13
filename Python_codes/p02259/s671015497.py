n = int(raw_input())
a = map(int,raw_input().split(' '))

nswap = 0
for i in range(n):
    for j in reversed(range(i+1,n)):
        if a[j] < a[j-1]:
            a[j],a[j-1]=a[j-1],a[j]
            nswap+=1

print ' '.join([str(v) for v in a])
print nswap