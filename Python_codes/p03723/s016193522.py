a,b,c = map(int,input().split())
if a==b==c and a%2==1:
    print(0)
elif a==b==c and a%2==0:
    print("-1")
else:
    cnt = 0
    while all(i&1==0 for i in [a,b,c]):
        A = a
        B = b
        C = c
        a = (B+C)//2
        b = (A+C)//2
        c = (A+B)//2
        cnt += 1
    print(cnt)
