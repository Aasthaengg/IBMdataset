a,b,x=map(int,input().split())
if a==0:
    #0以上b以下でbで割り切れる個数
    if b%x==0:
        ans_b = b//x +1
    else:
        ans_b = b//x +1
    #0以上a未満でbで割り切れる個数
    if a%x==0:
        ans_a = a//x
    else:
        ans_a = a//x + 1
else:
    ans_b = b//x
    if a%x==0:
        ans_a = a//x -1
    else:
        ans_a = a//x

print(ans_b-ans_a)