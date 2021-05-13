n = int(input())
if n % 2 == 0:
    k = 1+n
    s = k*(n//2-1)
else:
    k = n
    s = k*(n//2)

ans = []
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if i+j == k:
            continue
        ans.append("{} {}".format(i, j))
print(len(ans))
print(*ans, sep='\n')
