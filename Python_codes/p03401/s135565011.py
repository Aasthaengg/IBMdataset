n = int(input())
s = list(map(int,input().split()))

ans = 0
tmp = 0
for i in range(n):
    ans += abs(s[i] - tmp)
    tmp = s[i]
ans += abs(tmp)

s.insert(0,0)
s.insert(n+1,0)
for i in range(1,n+1):#とばす番号
    tmp_ans = ans
    a = s[i-1]
    tmp = s[i]
    b = s[i+1]
    if (b >= tmp and tmp >= a) or (b <= tmp and tmp <= a):
        pass
    else:
        if (a >= b and tmp > a) or (a <= b and tmp < a):
            tmp_ans -= abs(2*(tmp-a))
        else:
            tmp_ans -= abs(2*(tmp-b))
    print(tmp_ans)