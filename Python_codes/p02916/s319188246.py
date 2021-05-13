n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

cnt=0
first_flg = True
for i in a:
    if not first_flg:
        if i-1 == before_num:
            cnt += c[i-2]
    first_flg = False
    before_num = i
print(sum(b)+cnt)    