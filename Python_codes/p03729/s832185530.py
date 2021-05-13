a,b,c = map(str,input().split())
count = 0
if a[-1] == b[0]:
    count += 1
if b[-1] == c[0]:
    count += 1
if count ==2:
    print('YES')
else:
    print("NO")