n = int(input())
total = 0
ans = []
for i in range(1, n+1):
    ans.append(i)
    total += i
    if total > n:
        break
ng = total - n
print(*[i for i in ans if i != ng], sep='\n')