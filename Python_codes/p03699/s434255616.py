N=int(input())
s=[int(input()) for _ in range(N)]
ss = [s[i] for i in range(N) if s[i]%10!=0]
if sum(s)%10 != 0:
    print(sum(s))
else:
    if not ss:
        print(0)
    else:
        print(sum(s) - min(ss))