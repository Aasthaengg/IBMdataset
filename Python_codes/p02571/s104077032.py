s = input()
t = input()
ans = len(t)

for i in range(len(s)-len(t)+1):
    count = 0
    for j in range(len(t)):
        if s[i+j]!=t[j]:
            count += 1
    # print(count)
    ans = min(ans, count)

print(ans)
