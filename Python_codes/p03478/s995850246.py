N, A, B = map(int, input().split())
total = 0
for i in range(N + 1):
    I = str(i)
    L = len(I)
    sum = 0
    for j in range(L):
        sum = sum + int(I[j])
    if A <= sum <= B:
        total = total + i
print(total)