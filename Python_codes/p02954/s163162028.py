s = input()
n = len(s)
# indごとの、次のLまでの距離
next_L = [0] * n
next_R = [0] * n
dist = 0
for i in range(n-1,-1,-1):
    if s[i] == 'R':
        dist += 1
        next_L[i] = dist
    else:
        dist = 0
dist = 0
for i in range(n):
    if s[i] == 'L':
        dist += 1
        next_R[i] = dist
    else:
        dist = 0
ans_ls = [0] * n
for i in range(n):
    if s[i] == 'R':
        if next_L[i] % 2 == 0:
            ans_ls[i+next_L[i]] += 1
        else:
            ans_ls[i+next_L[i]-1] += 1
for i in range(n-1,-1,-1):
    if s[i] == 'L':
        if next_R[i] % 2 == 0:
            ans_ls[i-next_R[i]] += 1
        else:
            ans_ls[i-next_R[i]+1] += 1
ans_ls = list(map(str,ans_ls))
print(' '.join(ans_ls))


