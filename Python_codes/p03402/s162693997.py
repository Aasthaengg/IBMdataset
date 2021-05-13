#!/usr/bin/env python3

def main():
    na = list(map(int, input().split()))
    A, B = na[0], na[1]

    mp = []
    for i in range(41):
        lst = []
        for j in range(41):
            lst.append(0)
        for j in range(41):
            lst.append(1)
        mp.append(lst)

    a = b = 1

    if a < A:
        for n in range(3, 39 + 3, 3):
            for i in range(n):
                if a < A:
                    mp[n - i][41 + i + 1] = 0
                    a += 1
                else:
                    break
            if A <= a:
                break
    if a < A:
        for n in range(36, 0, -3):
            for i in range(n):
                if a < A:
                    mp[39 - i][41 + 39 - n + i + 1] = 0
                    a += 1
                else:
                    break
            if A <= a:
                break
    if b < B:
        for n in range(3, 39 + 3, 3):
            for i in range(n):
                if b < B:
                    mp[n - i][i + 1] = 1
                    b += 1
                else:
                    break
            if B <= b:
                break
    if b < B:
        for n in range(36, 0, -3):
            for i in range(n):
                if b < B:
                    mp[39 - i][39 - n + i + 1] = 1
                    b += 1
                else:
                    break
            if B <= b:
                break


    print('41 82')
    for lst in mp:
        s = ''
        for v in lst:
            s += '#' if v == 1 else '.'
        print(s)

if __name__ == '__main__':
    main()

