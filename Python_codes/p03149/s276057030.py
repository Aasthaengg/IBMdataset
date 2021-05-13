#%%
l = list(map(int, input().split()))
l.sort()
for i in range(len(l)):
        l[i] = str(l[i])
a = ''.join(l)
if a == '1479':
        print('YES')
else:
        print('NO')

