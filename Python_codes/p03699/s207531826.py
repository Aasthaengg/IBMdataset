N=int(input())
s=[int(input())for i in range(N)]
sum_s=sum(s)
if sum_s%10!=0:
    print(sum_s)
    exit()
else:
    ss=sorted(s)
    for i in range(N):
        if (sum_s-ss[i])%10!=0:
            print(sum_s-ss[i])
            exit()
print(0)