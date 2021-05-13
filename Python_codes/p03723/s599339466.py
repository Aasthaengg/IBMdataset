cookie = list(map(int,input().split()))
odd = False
cnt = 0
if cookie[0]%2==1 or cookie[1]%2== 1 or cookie[2]%2==1:
    print(0)
elif len(list(set(cookie))) == 1:
    print('-1')
else:
    while not odd:
        tmp = [0 for i in range(3)]
        for i in range(3):
            ix = list(set([0,1,2]) - set([i]))
            tmp[ix[0]] += cookie[i] / 2
            tmp[ix[1]] += cookie[i] / 2
        for i in tmp:
            if not i % 2 == 0:
                odd = True
        cookie = tmp
        cnt += 1
    print(cnt)