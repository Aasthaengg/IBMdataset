def solve():
    M, K = [int(_) for _ in raw_input().split()]
    if M == 0:
        if K == 0:
            print '0 0'
        else:
            print '-1'
    elif M == 1:
        if K == 0:
            print  '0 0 1 1'
        else:
            print '-1'
    else:
        MAX = 1 << M
        if K >= MAX:
            print '-1'
        else:
            arr = list(range(K))
            arr.extend(list(range(K + 1, MAX)))
            arr_rev = arr[::-1]
            arr.append(K)
            arr.extend(arr_rev)
            arr.append(K)
            for ele in arr:
                print ele,

if __name__ == '__main__':
    solve()
