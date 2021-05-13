from collections import Counter

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    T = list(input())
    l = list()
    ans = 0
    for i in range(k):
        l.append(T[i])
    for i in range(k, n):
        if l[i-k] == T[i]:
            l.append(None)
        else:
            l.append(T[i])
    res = Counter(l)
    ans = res['r'] * p + res['s'] * r + res['p'] * s
    print(ans)

if __name__ == '__main__':
    main()