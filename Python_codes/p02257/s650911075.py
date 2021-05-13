N = input()
sum = 0
for _ in xrange(N):
    n = input()
    for i in xrange(2,n):
        if i > n/i:
            sum += 1
            break
        if n%i == 0:
            break
    else:
        sum += 1
print sum