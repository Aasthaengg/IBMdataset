n = int(input())
check = []
ans = 0
for _ in range(n):
    n1, n2 = map(int, input().split())
    if n1 == n2:
        check.append(1)
    else:
        check.append(0)

for i in range(n-1):
    if sum(check[i:i+3])==3:
        ans = 1
        break
if ans:
    print("Yes")
else:
    print("No")