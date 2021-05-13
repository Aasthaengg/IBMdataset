inf = 10**15
mod = 10**9+7
n, k = map(int, input().split())
s = input()
count = 0
flag = False
for c in s:
    if c == 'R':
        if flag == False:
            flag=True
    else:
        if flag == True:
            count+=1
            flag=False
if s[-1]=='R' and count > 0:
    count+=1

if k >= count:
    print(n-1)
elif k == count-1:
    if s[0] == 'R' and s[-1] == 'R':
        print(n-1)
    elif s[0] == 'R' or s[-1] == 'R':
        print(n-2)
    else:
        print(n-3)
else:
    if s[0] == 'R' and s[-1] == 'R':
        print(n - 3 - (count - 2 - k) * 2)
    elif s[0] == 'R' or s[-1] == 'R':
        print(n - 2 - (count - 1 - k) * 2)
    else:
        print(n - 1 - (count - k) * 2)
