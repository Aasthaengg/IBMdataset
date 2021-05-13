h,w = map(int,input().split())
aij = [input() for i in range(h)]

def moji_num(s):
    return ord(s) - ord('a')

if h % 2 == 0:
    if w % 2 == 0:
        pat = 1
    else:
        pat = 2
else:
    if w % 2 == 0:
        pat = 3
    else:
        pat = 4

moji = [0]*(26)

for i in range(h):
    for j in range(w):
        moji[moji_num(aij[i][j])] += 1
        
#print(moji)

b1 = 0
b2 = 0

for i in range(26):
    if moji[i] % 2 == 1:
        tmp = moji[i]
        if tmp % 4 == 3:
            b2 += 1
        #b1_li.append(moji_num(moji[i]))
        b1 += 1
        #print(i)
    elif moji[i] % 2 == 0 and moji[i] % 4 != 0:
        b2 += 1


#print(pat,b1,b2)        
        
if b1 > 1:
    print('No')
    exit()
elif pat == 1:
    if b2 > 0:
        print('No')
        exit()
elif pat == 2:
    if b2 > h//2:
        print('No')
        exit()
elif pat == 3:
    if b2 > w//2:
        print('No')
        exit()
elif pat == 4:
    if b2 > (h+w-2)//2:
        print('No')
        exit()

print('Yes')