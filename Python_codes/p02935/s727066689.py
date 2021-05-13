N = int(input())
v = list(map(int,input().split()))

v.sort()

total = 0
for i in range(N):
    if i == 0:
        total +=v[i] * 1/(2**(N-i-1))
    else:
        total +=v[i] * 1/(2**(N-i))

print(total)