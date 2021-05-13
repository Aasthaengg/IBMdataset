N = int(input())
ans = float('inf')
for i in range(1, N):
    j = N-i
    i_str = str(i)
    j_str = str(j)
    i_sum, j_sum = 0, 0
    for p in range(len(i_str)):
        i_sum += int(i_str[p])
    for q in range(len(j_str)):
        j_sum += int(j_str[q])
    ans = min(ans, i_sum+j_sum)

print(ans)
