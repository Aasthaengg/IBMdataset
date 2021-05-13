import sys
read = sys.stdin.read
def main():
    n, q = map(int, input().split())
    s = input()
    acs = [0] * (n + 1)
    cnt = 0
    for i1 in range(1, n):
        if s[i1-1] =='A' and s[i1] == 'C':
            cnt += 1
        acs[i1+1] = cnt
    for _ in range(q):
        l, r = map(int, input().split())
        r = acs[r] - acs[l]
        print(r)


if __name__ == '__main__':
    main()
