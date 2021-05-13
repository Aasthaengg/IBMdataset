a, b, k = map(int, input().split())
ans = []
for i in range(1, a*b + 1):
    if a%i == 0 and b%i == 0:
        ans.append(i)
print(ans[-1*k])
