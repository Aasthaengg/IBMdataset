s = input()
ss = set(s)
flg = True

if len(ss) != 2:
    flg = False

for i in ss:
    if s.count(i) != 2:
        flg = False
    
print('Yes') if flg else print('No')