
def CODE_festival_2016_A():
    import numpy as np
    N = int(input())
    a = np.array(list(map(int,input().split())))

    ans = 0
    for i in range(N):
        if i == a[a[i]-1]-1:
            ans += 1

    print(int(ans) if ans%2==1 else int(ans/2))


CODE_festival_2016_A()