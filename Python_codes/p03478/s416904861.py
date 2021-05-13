N, A, B = map(int, input().split())

sum = 0

for n in range(1, N+1):
    nsum = 0
    m = n
    while m != 0:
        nsum += m % 10
        m = m//10
    if nsum >= A and nsum <= B:
        sum += n
print(sum)
