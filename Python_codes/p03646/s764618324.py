k = int(input())

n = 50
ans = [i for i in range(n)]

for i in range(n):
    ans[i] += k // n

for i in range(k % n):
    ans[i] += n
    for j in range(n):
        if i == j:
            continue
        ans[j] -= 1

print(n)
a = [str(x) for x in ans]
print(' '.join(a))
