h, w = map(int, input().split())

f = (h-h%2)*(w-w%2)//4
t = 0
one = 0
if h%2==1:
    t += w//2
if w%2==1:
    t += h//2
if h%2==1 and w%2==1:
    one = 1

dic = {}
for i in range(h):
    a = list(input())
    for j in a:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1

result = True
for i, j in dic.items():
    if j%2==1:
        if one == 1:
            j -= 1
            one -= 1
        else:
            result = False
    if j==0:
        continue
    while f > 0 and j>=4:
        j -= 4
        f -= 1
        if j==0:
            break
    if j==0:
        continue
    while t > 0 and j>=2:
        j -= 2
        t -= 1
        if j==0:
            break
    if j==0:
        continue
    else:
        result = False

    if result == False:
        break

if result:
    print("Yes")
else:
    print("No")