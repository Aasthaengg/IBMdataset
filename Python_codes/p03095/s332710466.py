from collections import Counter
def main():
    n = int(input())
    s = input()
    mod = 1000000007
    c = Counter(s)
    ans = 1
    for v in c.values():
        ans = ans * (v + 1) % mod
    print(ans - 1)
if __name__ == '__main__':
    main()
