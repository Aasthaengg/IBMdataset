n = int(input())
s = input()
R_ls = [0] * n
G_ls = [0] * n
B_ls = [0] * n
R_csum = [0] * n
G_csum = [0] * n
B_csum = [0] * n
for i in range(n):
    if s[i] == 'R':
        R_ls[i] = 1
        R_csum[i] = R_csum[i-1] + 1
        G_csum[i] = G_csum[i-1]
        B_csum[i] = B_csum[i-1]
    elif s[i] == 'G':
        G_ls[i] = 1
        G_csum[i] = G_csum[i-1] + 1
        R_csum[i] = R_csum[i-1]
        B_csum[i] = B_csum[i-1]
    else:
        B_ls[i] = 1
        B_csum[i] = B_csum[i-1] + 1
        R_csum[i] = R_csum[i-1]
        G_csum[i] = G_csum[i-1]
ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        if (s[i] == 'R' and s[j] == 'G') or (s[i] == 'G' and s[j] == 'R'):
            now = B_csum[-1] - B_csum[j]
            if j + (j-i) < n and s[2*j-i] == 'B':
                now -= 1
        elif (s[i] == 'R' and s[j] == 'B') or (s[i] == 'B' and s[j] == 'R'):
            now = G_csum[-1] - G_csum[j]
            if j + (j-i) < n and s[2*j-i] == 'G':
                now -= 1
        elif (s[i] == 'G' and s[j] == 'B') or (s[i] == 'B' and s[j] == 'G'):
            now = R_csum[-1] - R_csum[j]
            if j + (j-i) < n and s[2*j-i] == 'R':
                now -= 1
        else:
            now = 0
        ans += now
print(ans)


