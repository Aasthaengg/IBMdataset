N = int(input())
L = list(map(int, input().split()))

count = 0

for k in range(N):
    for j in range(N):
        for i in range(N):
            if i>=j or j>=k:
                continue
            l = sorted([L[i], L[j], L[k]])
            if l[0] == l[1] or l[1] == l[2]:
                continue
            if l[2] < l[0] + l[1]:
                count += 1


print(count)