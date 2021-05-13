N = int(input())
ans = 0
dic = {'A':0, 'B':0, 'BA':0}
for i in range(N):
    tmp = input()
    if 'AB' in tmp:
        ans += tmp.count('AB')
    tmp = tmp.replace('AB','ZZ')
    if tmp[-1] == 'A' and tmp[0] == 'B':
        dic['BA'] += 1
    elif tmp[0] == 'B':
        dic['B'] += 1
    elif tmp[-1] == 'A':
        dic['A'] += 1

if dic['B'] >= 1 and dic['A'] >= 1 and dic['BA'] >= 1:
    ans += dic['BA'] + 1
    dic['BA'] = 0
    dic['B'] -= 1
    dic['A'] -= 1
if dic['BA'] >= 1:
    if dic['A'] == 0 and dic['B'] == 0:
        ans += dic['BA'] - 1
    elif dic['A'] == 0 or dic['B'] == 0:
        ans += dic['BA']
else:
    ans += min(dic['A'],dic['B'])
print(ans)