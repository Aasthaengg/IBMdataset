n = int(input())
a = list(map(int,input().split()))

d = {'gry':0,'brw':0,'grn':0,'miz':0,'blu':0,'yel':0,'dai':0,'red':0,'any':0}
for i in a:
    if 1 <= i <= 399:
        d['gry'] += 1
    elif 400 <= i <= 799:
        d['brw'] += 1
    elif 800 <= i <= 1199:
        d['grn'] += 1
    elif 1200 <= i <= 1599:
        d['miz'] += 1
    elif 1600 <= i <= 1999:
        d['blu'] += 1
    elif 2000 <= i <= 2399:
        d['yel'] += 1
    elif 2400 <= i <= 2799:
        d['dai'] += 1
    elif 2800 <= i <= 3199:
        d['red'] += 1
    else: #any
        d['any'] += 1

ans = 0
zero = 0
for k,v in d.items():
    if k == 'any':
        pass
    else:
        if v != 0:
            ans += 1

print (max(1,ans),ans+d['any'])
