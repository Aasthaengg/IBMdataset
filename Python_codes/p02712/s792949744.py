N = int(input())
ans = []

for i in range(N+1):
    if i % 3 != 0 and i % 5 != 0:
        ans.append(i)

print(sum(ans))