N = int(input())
bar = list(map(int, input().split()))
triangles = []
for i in range(N-2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if (bar[i] + bar[j] > bar[k]) and (bar[j] + bar[k] > bar[i]) and (bar[i] + bar[k] > bar[j]) and (len(set([bar[i], bar[j], bar[k]])) == 3):
                triangles.append([bar[i], bar[j], bar[k]])
print(len(triangles))
