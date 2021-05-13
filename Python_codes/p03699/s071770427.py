N=int(input())
s=[int(input()) for i in range(N)]
s.sort()
ans = sum(s)
if ans%10!=0:
    print(ans)
    exit()
else:
    for i in s:
        ans2 = ans-i
        if ans2%10!=0:
            print(ans2)
            exit()
print(0)