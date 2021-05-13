n = int(input())
mydict = {}
for _ in range(n):
    tmp=sorted(input(), key=str.lower)
    tmp = ''.join(sorted(tmp))
    if tmp in mydict:
        mydict[tmp]+=1
    else:
        mydict.setdefault(tmp, 1)
ans = 0
for i in mydict.values():
    ans+=i*(i-1)/2
print(int(ans))

