t=list((set(list(str(input())))))
t.sort(reverse=False)
al = ('abcdefghijklmnopqrstuvwxyz')
alll=list(al)
for a in alll:
    if a not in t:
        print(a)
        exit()
print('None')