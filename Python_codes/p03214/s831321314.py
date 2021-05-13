N = int(input())
A = list(map(int, input().split()))
ave = sum(A) / len(A)
diff = float('inf')
ans = None
for i, a in enumerate(A):
    if abs(a - ave) < diff:
        diff = abs(a - ave)
        ans = i
print(ans)