M,K = map(int,input().split())
if K>=2**M:
    print(-1)
elif M==1:
    if K==0:
        print('0 0 1 1')
    else:
        print(-1)
else:
    ans1 = [i for i in range(2**M) if i != K]
    ans2 = ans1[::-1]
    ans = [K]+ans1+[K]+ans2
    ans = ' '.join(str(i) for i in ans)
    print(ans)