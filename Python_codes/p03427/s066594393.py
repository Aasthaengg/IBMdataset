n = input()
ans = 0
accu = 0
for i, j in enumerate(n):
    j = int(j)
    if j>0:
        ans = max(ans, accu+j-1+9*(len(n)-i-1))
    accu += j
ans = max(ans, accu)
print(ans)