s = input()
n = len(s)
interval = n - 7
flag = False
start = 0
end = interval
for i in range(n-interval):
    news = s[0:start] + s[end:]
    if news == 'keyence':
        print('YES')
        flag = True
        break
    start+=1
    end+=1
if not flag:
    print('NO')