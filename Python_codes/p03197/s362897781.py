#%%
n = int(input())
a = [0] * n
flag = True
for i in range(n):
    a[i] = int(input())
    if a[i] % 2 == 1:
        flag = False

if not flag:
    print('first')
else:
    print('second')