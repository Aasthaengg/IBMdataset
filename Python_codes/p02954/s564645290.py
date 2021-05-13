s = list(input())
s.append('R')
ans = [0] * (len(s)-1)
Rc = 0
Lc = 0
for i in range(len(s)) :
    if Lc != 0 and s[i] == 'R' :
        ans[Ri] = Rc % 2 + Rc // 2 + Lc // 2
        ans[Ri+1] = Rc//2 + Lc//2 + Lc%2
        Rc = 1
        Ri = i
        Lc = 0
    elif s[i] == 'R' :
        Rc += 1
        Ri = i
    elif s[i] == 'L':
        Lc += 1

ans = ' '.join([str(n) for n in ans])
print(ans)