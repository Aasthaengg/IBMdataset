s = list(input())
k = int(input())
num = len(s)
ans = 0

if len(set(s))==1:
    print(num*k//2)
else:
    now = s[0]
    cnt = 1
    fstflag = True
    for i in range(1,num):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            ans += (cnt//2)*k
            if fstflag:
                fstflag = False
                begin = cnt
            cnt = 1
    ans += (cnt//2)*k
    if fstflag:
        fstflag = False
        begin = cnt
    if s[0] == s[-1]:
        end = cnt
        ans -= (begin//2)*(k-1)
        ans -= (end//2)*(k-1)
        ans += ((begin+end)//2)*(k-1)
    print(ans)