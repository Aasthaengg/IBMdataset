n = int(input())
s = input()
ans = 0

for i in range(1, n):
    a = s[:i]
    b = s[i:]
    a_al = []
    ans_t = 0

    for k in range(len(a)):
        for l in range(len(b)):
            if a[k] in a_al:
                continue
            if a[k] == b[l]:
                ans_t += 1
                a_al.append(a[k])
    if ans_t > ans:
        ans = ans_t

print(ans)
