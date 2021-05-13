n = int(input())
s = input()

ans_list = []
for i in range(n):
    ans = 0
    x = list(set(s[:i]))
    y = list(set(s[i:]))
    for j in range(len(x)):
        if x[j] in y:
            ans += 1
    ans_list.append(ans)

a = max(ans_list)
print(a)