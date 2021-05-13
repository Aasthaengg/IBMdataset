N, A, B = map(int, input().split())
X = list(map(int, input().split()))

X.sort()

group=[[X[0]]]
for i in range(N-1):
    if (X[i+1] - X[i]) * A > B:
        group.append([X[i+1]])
    else:
        group[-1].append(X[i+1])
#print(group)

ans = (len(group) - 1) * B
for g in group:
    ans += (max(g) - min(g)) * A
print(ans)