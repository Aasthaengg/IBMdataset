n=int(input())
s=list(int(input()) for _ in range(n))
k=sum(s)
s.sort()
if k%10==0:
    for i in s:
        if i%10!=0:
            print(k-i)
            exit()
    print(0)
else:
    print(k)

