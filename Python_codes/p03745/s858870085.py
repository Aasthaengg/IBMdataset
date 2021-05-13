n = int(input())
a = list(map(int,input().split()))
b = []
flg = 'hi'
for i in range(n-1):
    if a[i] > a[i+1]:
        if flg != 'pl':
            flg = 'mi'
        else:
            b.append(i)
            flg = 'hi'
    elif a[i] < a[i+1]:
        if flg != 'mi':
            flg = 'pl'
        else:
            b.append(i)
            flg = 'hi'
print(len(b)+1)