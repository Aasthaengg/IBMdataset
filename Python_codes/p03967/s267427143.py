s = input()
N = len(s)

win = lose = 0
g = p = 0

for i in range(N):
    if s[i]=="g":
        if p < g:
            p += 1
            win += 1
        else:
            g += 1
    else: # s[i]=="p"
        if p < g:
            p += 1
        else:
            g += 1
            lose += 1
print(win-lose)
