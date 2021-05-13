num = int(input())
work = []
for i in range(num):
    work.append(list(map(int,input().split(' '))))
work.sort(key = lambda a: a[1])
time = 0
limit  = 0
cant_flg = 0
for w in work:
    limit = w[1]
    time += w[0]
    if(limit<time):
        print('No')
        cant_flg = 1
        break
if(cant_flg==0):
    print('Yes')
