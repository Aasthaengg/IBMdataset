n,x = map(int,input().split())
a_lst = sorted(list(map(int,input().split())))

cnt = 0

if x == sum(a_lst):
    print(len(a_lst))
elif x > sum(a_lst):
    print(len(a_lst)-1)
else:
    for i in a_lst:
        x -= i
        if x < 0:
            break
        cnt += 1
    print(cnt)