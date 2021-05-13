n=int(input())
s=[int(input()) for i in range(n)]

s.sort()
S=sum(s)

if S%10!=0:
    print(S)
else:
    for num in s:
        if num%10!=0:
            S-=num
            if S%10!=0:
                print(S)
                exit()

    print(0)  