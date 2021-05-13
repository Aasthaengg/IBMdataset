N, M = map(int, input().split())
total = 0
for A in input().split():
    total = total+int(A)
if total > N:
    ans = -1
else:
    ans = N-total
print(ans)
