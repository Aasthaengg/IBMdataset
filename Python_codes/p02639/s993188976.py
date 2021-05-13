lis = input().split()
i = lis.index('0')

if i==0:
    ans = int(lis[1])-1
    print(ans)
else:
    ans = int(lis[i-1])+1
    print(ans)