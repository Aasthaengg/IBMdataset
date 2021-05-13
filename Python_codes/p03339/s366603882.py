n = int(input())
s = input()

w_e = [0] * n
e_w = [0] * n
ans = []

for i in range(n - 1):
    if s[i] == 'W':
        w_e[i + 1] = w_e[i] + 1
    else:
        w_e[i + 1] = w_e[i] + 0

for i in range(n - 2, -1, -1): 
    if s[i + 1] == 'E':
        e_w[i] = e_w[i + 1] + 1
    else:
        e_w[i] = e_w[i + 1] + 0

for i in range(n):
    ans.append(w_e[i] + e_w[i])

print(min(ans))