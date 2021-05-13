s = list(input())
cnt = 0
for i in range(len(s)):
    if i % 2 == 0 and s[i] in ['R', 'U', 'D']:
        cnt += 1
    elif i % 2 == 1 and s[i] in ['L', 'U', 'D']:
        cnt += 1
print('Yes' if cnt == len(s) else 'No')