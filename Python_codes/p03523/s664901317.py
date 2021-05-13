S = input()
let = ['KIH','B','R','']
ans = 'NO'
for i in range(2**4):
    cand = ''
    for j in range(4):
        if (i >> j) & 1 == 1:
            cand += 'A'
        cand += let[j]
    if cand == S:
        ans = 'YES'
        break
print(ans)