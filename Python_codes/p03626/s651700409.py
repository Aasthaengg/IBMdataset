def solve():
    mod = 10**9+7
    N = int(input())
    s1 = input()
    s2 = input()
    lis = []
    i=0
    while i<N-1:
        if s1[i]==s1[i+1]:
            lis.append(2)
            i += 2
        else:
            lis.append(1)
            i += 1
    if i==N-1:
        lis.append(1)
    if lis[0]==1:
        ans = 3
    else:
        ans = 6
    for i in range(len(lis)-1):
        if lis[i]==1:
            ans *= 2
            ans %= mod
        if lis[i]==2 and lis[i+1]==2:
            ans *=3
            ans %= mod
    return ans
print(solve())