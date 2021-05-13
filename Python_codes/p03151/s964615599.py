N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

l = []
h = []

for i in range(N):
    if A[i] < B[i]:
        l.append(B[i]-A[i])
    else:
        h.append(A[i]-B[i])

h.sort()

res = 0
y = 0
for x in l:
    while x > y:
        if h:
            res += 1
            y += h.pop()
        else:
            print(-1)
            exit()
    
    res += 1
    y -= x

print(res)