s, t = input(), input()
ret = len(t)
for i in range(len(s)-len(t)+1):
    u = s[i:len(t)+i]
    count_diff = 0
    for j in range(len(u)):
        if u[j] != t[j]:
            count_diff += 1
    ret = min(ret, count_diff)
print(ret)