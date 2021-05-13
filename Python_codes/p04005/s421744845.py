A = sorted(list(map(int, input().split())))
ans = A[0]*A[1]
for a in A:
    if a%2==0: ans = 0
print(ans)