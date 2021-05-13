N = int(input())

s = int(N*(N+1)/2)
for k in range(2,N+1):
    i = 1
    while k*i <= N:
        s += k*i
        i += 1

print(s)