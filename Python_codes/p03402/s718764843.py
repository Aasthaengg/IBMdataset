a,b = map(int,input().split())
li = []
for i in range(100*100):
    h = i//100
    w = i%100
    if(w<50):
        li.append('.')
    else:
        li.append('#')
nokori = b-1
for i in range(100):
    if(nokori == 0):
        break
    if(i%2 == 1):
        continue
    for j in range(50):
        if(j%2 == 1):
            continue
        if(nokori == 0):
            break
        nokori -= 1
        li[i*100+j]='#'
nokori = a-1
for i in range(100):
    if(nokori == 0):
        break
    if(i%2 == 0):
        continue
    for j in range(50,100):
        if(j%2 == 0):
            continue
        if(nokori == 0):
            break
        nokori -= 1
        li[i*100+j]='.'
print(100,100)
ans = ["" for i in range(100)]
for i in range(100):
    for j in range(100):
        ans[i] += li[i*100+j]
for hoge in ans:
    print(hoge)
