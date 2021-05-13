N=int(input())
d_pre=input().split()
d=[int(s) for s in d_pre]
d.sort()
d_2=d[::-1]
ans=1
if 0 in d_2:
    print(0)
else:
    for i in range(N):
        ans*=d_2[i]
        if ans>10**18:
            print(-1)
            break
        elif i==N-1:
            print(ans)