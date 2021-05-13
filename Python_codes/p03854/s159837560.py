S = input()
n = len(S)
T = ['dreamer', 'eraser', 'dream', 'erase']
idx = n
res = 'YES'
while idx > 0:
    for t in T:
        if S[idx-len(t):idx] == t:
            idx -= len(t)
            break
    else:
        res = 'NO'
        idx = -1
print(res)