a,b = map(int,input().split())

cnt=0
for i in range(a,b+1):
    a = list(str(i))
    a.reverse()
    a="".join(a)
    if a == str(i):
        cnt += 1
    else:
        continue
print(cnt)