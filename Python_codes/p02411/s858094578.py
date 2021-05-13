from sys import stdin

def main():
    for l in stdin:
        m ,f, r = map(int, l.split(' '))

        if -1 == m == f == r:
            break

        print(judge(m, f, r))

def judge(m, f, r):
    if -1 == m or -1 == f:
        return 'F'

    if 80 <= m+f:
        return 'A'

    if 65 <= m+f < 80:
        return 'B'

    if 50 <= m+f < 65:
        return 'C'

    if 30 <= m+f < 50:
        return 'C' if 50 <= r else 'D'

    return 'F'

if __name__ == '__main__': main()