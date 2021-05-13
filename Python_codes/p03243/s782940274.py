n = int(input())
v = [999,888,777,666,555,444,333,222,111]
ans = 0
for i in range(9):
    if v[i] >= n:
        ans = v[i]
print(ans)