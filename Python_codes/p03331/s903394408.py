n = int(input())
ans = 1001001001
for i in range(1,n):
    j = n-i
    i_sum, j_sum = 0, 0

    si, sj = list(str(i)), list(str(j))
    for s1 in si:
        i_sum += int(s1)
    for s2 in sj:
        j_sum += int(s2)

    ans = min(ans, i_sum+j_sum)

print(ans)