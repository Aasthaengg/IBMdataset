def f(k):
    T = S*k
    N = len(T)
    cur = T[0]
    cnt = 1
    ans = 0
    for i in range(1,N):
        if T[i]==cur:
            cnt += 1
        else:
            ans += cnt//2
            cur = T[i]
            cnt = 1
    ans += cnt//2
    return ans
S = input().strip()
K = int(input())
ans1 = f(1)
ans2 = f(2)
ans3 = f(3)
d1 = f(2)-f(1)
d2 = f(3)-f(2)
k = (K-1)//2
if (K-1)%2==0:
    print(f(1)+(d1+d2)*k)
else:
    print(f(1)+(d1+d2)*k+d1)