h, w = map(int, input().split())
a = []
for _ in range(h):
    a.append(input())
cnt = [0]*26
for i in a:
    for j in i:
        cnt[ord(j)-ord('a')] += 1

if h%2==0 and w%2==0:
    for i in cnt:
        if i%4!=0:
            print('No')
            break
    else:
        print('Yes')
elif h%2==0 or w%2==0:
    mod2 = 0
    for i in cnt:
        if i%2!=0:
            print('No')
            break
        elif i%4!=0:
            mod2 += i%4
    else:
        tmp = h if h%2==0 else w
        if mod2<=tmp:
            print('Yes')
        else:
            print('No')
else:
    mod2 = 0
    alone = False
    for i in cnt:
        if i%2!=0:
            if alone:
                print('No')
                break
            alone = True
            mod2 += (i%4)//2
        elif i%4!=0:
            mod2 += i%4
    else:
        if mod2<=h+w-2:
            print('Yes')
        else:
            print('No')