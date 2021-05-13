n = int(input())
l_list = list(map(int, input().split()))
l_list.sort()
ans = 0

for i in range(len(l_list)):
    for j in range(i + 1, len(l_list)):
        for k in range(j + 1, len(l_list)):
            if l_list[i] + l_list[j] > l_list[k] \
                    and l_list[i] != l_list[j] \
                    and l_list[j] != l_list[k] \
                    and l_list[k] != l_list[i]:
                ans += 1
print(ans)