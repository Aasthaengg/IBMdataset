#!/usr/bin/env python3.4

# abc126_f

def main():
    # input
    m, k = [int(s) for s in input().split()]
    n = 2**m
    #
    if k >= n:
        print('-1')
        return
    elif m == 0 and k == 0:
        print('0 0')
        return
    elif m == 1 and k == 0:
        print('0 0 1 1')
        return
    elif m == 1 and k == 1:
        print('-1')
        return
    # get ans
    l = [i for i in range(n) if i!=k]
    ans = []
    ans.extend(l)
    ans.append(k)
    ans.extend(reversed(l))
    ans.append(k)
    # output
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()

