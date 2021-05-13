def ABC046_B():
    import numpy as np
    n,k = map(int,input().split())


    for i in range(n):
        ans = k*np.power(k-1,n-1)

    print(ans)
    

ABC046_B()