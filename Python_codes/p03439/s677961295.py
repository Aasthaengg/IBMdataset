n = int(input())
a,b = 0, n
print(a,flush=True)
s = str(input())
if s == 'Vacant':
        exit()
for i in range(19):
    check = (a+b) // 2
    print(check,flush=True)
    t = str(input())
    if t == 'Vacant':
        exit()
    if (check-a) % 2 == 0 and s == t:
        a = check
    elif (check-a) % 2 == 0 and s != t:
        b = check
    elif s == t:
        b = check
    else:
        a,s = check,t