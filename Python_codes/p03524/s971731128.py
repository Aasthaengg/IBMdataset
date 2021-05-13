import collections
def main():
    s = list(input())
    tmp = len(set(s))
    c = collections.Counter(s)

    a_n = c['a']
    b_n = c['b']
    c_n = c['c']
    ans = []
    if len(s) == 1:
        print('YES')
        return
    if a_n >= b_n and a_n >= c_n:
        ans.append('a')
        a_n -= 1
        if b_n >= c_n:
            ans.append('b')
            b_n -= 1
        else:
            ans.append('c')
            c_n -= 1
    elif b_n >= a_n and b_n >= c_n:
        ans.append('b')
        b_n -= 1
        if a_n >= c_n:
            ans.append('a')
            a_n -= 1
        else:
            ans.append('c')
            c_n -= 1
    else:
        ans.append('c')
        c_n -= 1
        if b_n >= a_n:
            ans.append('b')
            b_n -= 1
        else:
            ans.append('a')
            a_n -= 1


    while True:
        if (ans[-1] == 'a' and ans[-2] == 'b') or (ans[-1] == 'b' and ans[-2] == 'a'):
            if c_n > 0 :
                c_n -= 1
                ans.append('c')
            else:
                if a_n == 0 and b_n == 0:
                    break
                print('NO')
                return
        elif (ans[-1] == 'c' and ans[-2] == 'b') or (ans[-1] == 'b' and ans[-2] == 'c'):
            if a_n > 0:
                a_n -= 1
                ans.append('a')
            else:
                if c_n == 0 and b_n == 0:
                    break
                print('NO')
                return
        else:
            if b_n > 0:
                b_n -= 1
                ans.append('b')
            else:
                if a_n == 0 and c_n == 0:
                    break
                print('NO')
                return
    print('YES')


if __name__ == '__main__':
    main()
