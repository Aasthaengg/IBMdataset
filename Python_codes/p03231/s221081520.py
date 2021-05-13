from fractions import gcd

def main():
    n, m = map(int, input().split())
    s = input().rstrip()
    t = input().rstrip()
    l = n*m // gcd(n, m)
    f = True
    for i in range(n):
        if i*m//n * n == i*m:
            j = i*m//n
            if s[i] != t[j]:
                f = False
    if f:
        print(l)
    else:
        print("-1")

if __name__ == "__main__":
    main()