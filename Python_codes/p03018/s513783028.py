s = input()

ss = s.replace('BC', '0').replace('A','1')

cnt = 0
ans = 0

for i in range(len(ss)-1, -1, -1):
    if ss[i] == 'B' or ss[i] == 'C':
        cnt = 0
    elif ss[i] == '1': ans += cnt
    else : cnt += 1
        
print(ans)
