#%%
n, k = map(int, input().split())
k = ['0'] * (42 - len(list(bin(k)[2:]))) + list(bin(k)[2:])
a = list(map(int, input().split()))

b = [[0] for _ in range(n)]
for i in range(n):
    b[i] = ['0'] * (42 - len(list(bin(a[i])[2:]))) + list(bin(a[i])[2:])

count = [[0, 0] for _ in range(42)]
for j in range(42):
    c_0, c_1 = 0, 0
    for i in range(n):
        if b[i][j] == '0':
            c_0 += 1
        else:
            c_1 += 1
    count[j] = c_0, c_1
        
ans = []
for i in range(42):
    if count[i][1] >= count[i][0]:
        ans.append('0')
    else:
        ans.append('1')

flag = False
for i in range(42):
    if ans[i] == '1' and k[i] == '0':
        ans[i] = '0'
    elif ans[i] == '0' and k[i] == '1':
        flag = True
    
    if flag:
        break

tmp = 0
ans = ans[::-1]
for i in range(42):
    if ans[i] == '1':
        tmp += 2**i

ans = 0
for i in range(n):
    ans += a[i] ^ tmp
print(ans)

