n, k, s = map(int, input().split())
if s == 1:
    ans = [s + 1] * n
else:
    ans = [s - 1] * n

for i in range(k):
    ans[i] = s
for num in ans:
    print(num, end = " ")
print()