# C - Green Bin
def main():
    import collections


    n = int(input())
    s = [''.join(sorted(input())) for _ in range(n)]
    c = collections.Counter(s)
    ans = 0
    
    for a in c:
        ans += (c[a] * (c[a] - 1)) //2
    print(ans)

if __name__ == '__main__':
    main()