n = int(input())
total = 0

A = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            B = [A[i], A[j], A[k]]
            if len(set(B)) == 3 and (max(B) < sum(B) - max(B)):
                total += 1

print(total)