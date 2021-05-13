n = int(input())
x = input()
ones = 0
for i in x:
    if i=='1':
        ones += 1
mods = [0, 0]
for i in range(n):
    if x[n-i-1]=='1':
        if ones>1:
            mods[0] += pow(2, i, ones-1)
        mods[1] += pow(2, i, ones+1)
if ones>1:
    mods[0] %= ones-1
mods[1] %= ones+1
def f(x):
    if x==0:
        return 1
    cnt = 1
    while x>0:
        p = bin(x).count('1')
        x %= p
        cnt += 1
    return cnt
for i in range(n-1, -1, -1):
    if x[n-i-1]=='1' and ones==1:
        print(0)
        continue
    if x[n-i-1]=='1':
        init = (mods[0] - pow(2, i, ones-1))%(ones-1)
    else:
        init = (mods[1] + pow(2, i, ones+1))%(ones+1)
    print(f(init))