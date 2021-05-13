N = int(input())
S = list(input())
x = 0
ls = []
ls.append(x)
for i in range(N):
    if S[i] == 'I':
        x += 1
        ls.append(x)
    elif S[i] == 'D':
        x -= 1
        ls.append(x)

print(max(ls))
