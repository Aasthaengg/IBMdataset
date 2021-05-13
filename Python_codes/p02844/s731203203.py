n = int(input())
s = input()
ans = 0
I = []
for i in range(n-2):
    if s[i] not in I:
        I.append(s[i])
    else:
        continue
    J = []
    for j in range(i+1, n-1):
        if s[j] not in J:
            J.append(s[j])
        else:
            continue
        K = []
        for k in range(j+1, n):
            if s[k] not in K:
                K.append(s[k])
                ans += 1
print(ans)