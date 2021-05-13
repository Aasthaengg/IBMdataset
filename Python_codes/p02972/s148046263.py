from sys import stdin

def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    p = []
    for i in reversed(range(n)):
        if a[i]:
            p.append(i + 1)
            u = 1
            v = i + 1
            while u * u <= v:
                if v % u == 0:
                    a[u - 1] ^= 1
                    if u != v // u:
                        a[v // u - 1] ^= 1
                u += 1
    if len(p) > 0:
        print(len(p))
        print(*p)
    else:
        print(0)
main()