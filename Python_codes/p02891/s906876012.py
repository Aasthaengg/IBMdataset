string = input()
k = int(input())

before = string[0]
flg = False
cnt = 0
if string.count(before) == len(string):
    print(len(string) * k // 2)
    exit()
for s in string[1:]:
    if s == before and not flg:
        cnt += 1
        flg = True
        continue
    flg = False
    before = s
ans = cnt * k
if string[0] == string[-1]:
    tmp = string[0]
    b_cnt = 0
    for s in string:
        if s == tmp:
            b_cnt += 1
        else:
            break
    a_cnt = 0
    for s in string[::-1]:
        if s == tmp:
            a_cnt += 1
        else:
            break
    if (a_cnt + b_cnt) % 2 == 0 and b_cnt % 2 == 1:
        ans += k - 1
        
    
print(ans)