def main():
    import itertools
    a,b,c,d = map(int,input().split())
    ans = -1 * float('inf')
    if a*c>ans:
        ans = a*c
    if a*d>ans:
        ans = a*d
    if b*c > ans:
        ans = b*c
    if b*d>ans:
        ans = b*d
    print(ans)

if __name__ == "__main__":
    main()
