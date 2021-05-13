import collections
n = int(input())
a = list(map(int,input().split()))
ac = collections.Counter(a)
ac = list(ac.items())
ac.sort()
# print(ac)

mod = int(1e9+7)
ans = 1
if n % 2 == 0:
    for i in range(1,n,2):
        if ac[i//2][0] != i or ac[i//2][1] != 2:
            print(0)
            exit()
        else:
            ans *= 2
            ans %= mod
else:
    for i in range(0, n, 2):
        if i == 0:
            if ac[i//2][0] != i or ac[i//2][1] != 1:
                print(0)
                exit()
        else:
            if ac[i//2][0] != i or ac[i//2][1] != 2:
                print(0)
                exit()
            else:
                ans *= 2
                ans %= mod
print(ans)


