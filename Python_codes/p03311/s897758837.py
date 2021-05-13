n = int(input())
list_A = list(map(int, input().split()))

for i in range(n):
    list_A[i] -= i + 1
list_A.sort()
b = 0
if n % 2 == 1:
    b = list_A[n//2]
else:
    b = (list_A[n//2]+list_A[n//2-1])//2

ans = 0

for num in list_A:
    ans += abs(num-b)

print(ans)