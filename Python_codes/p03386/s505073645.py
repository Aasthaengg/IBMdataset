a, b, k = map(int, input().split())
ans_list = list()
for i in range(a, min(a + k, b + 1)):
    ans_list.append(str(i))
for j in range(max(a, b - k + 1), b + 1):
    if str(j) not in ans_list:
        ans_list.append(str(j))
print("\n".join(ans_list))
