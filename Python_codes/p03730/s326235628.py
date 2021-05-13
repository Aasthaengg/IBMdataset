A,B,C=list(map(int,open(0).read().split()))
modlist=[A%B]
i=2

#あまりのリストを生成
while True:
    divd=A*i
    if divd%B==A%B:
        break
    modlist.append(divd%B)
    i=i+1

for j in modlist:
    if j==0:
        continue
    if C%j==0:
        print('YES')
        break
    else:
        C=C%j
else:
    print('NO')