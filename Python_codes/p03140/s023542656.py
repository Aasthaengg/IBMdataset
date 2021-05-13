n =int(input())
A = [x for x in list(str(input()))]
B = [x for x in list(str(input()))]
C = [x for x in list(str(input()))]
ans = 0

for i in range(n):
    if A[i] != B[i] and A[i] != C[i] and B[i] != C[i]:
        ans += 2
    elif A[i] == B[i] and A[i] == C[i] and B[i] == C[i]:
        ans += 0
    else:
        ans += 1

print(ans)