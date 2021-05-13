[n,m] = [int(i) for i in input().split()]
if n == 1:
    print(m)
else:
    ans = -1
    #a1は高々この値
    a1_max = m // n
    for i in range(a1_max,0,-1):
        if (m - i) % i == 0 and (m - i)//i >= (n-1):
            ans = max(ans,i)
    print(ans)
