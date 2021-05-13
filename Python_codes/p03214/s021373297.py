N = int(input())
A = list(map(int,input().split()))
mid = sum(A)/N
diff = []
for i in range(N):
    diff.append(abs(mid-A[i]))
print(diff.index(min(diff)))
