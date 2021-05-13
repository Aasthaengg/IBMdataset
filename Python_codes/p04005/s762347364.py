A, B, C = sorted(map(int,input().split()))

if A % 2 != 0 and B % 2 != 0 and C % 2 != 0:
    
    tmp1 = A * B
    tmp2 = C // 2
    tmp3 = C - tmp2
    ans = tmp1 * tmp3 - tmp1 * tmp2
    print(ans)
else:
    print(0)