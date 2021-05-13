n=int(input())
s=sorted([int(input()) for _ in range(n)])

su=sum(s)

if su%10>0:
    print(su)
else:
    for i in range(n):
        if s[i]%10>0:
            print(su-s[i])
            break
    else:
        print(0)