N = map(int, input())

num = list(N)
su = 0


for i in num:
    su += i

if su%9 == 0:
    print('Yes')
else:
    print('No')