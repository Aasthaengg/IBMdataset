def resolve():
    N = int(input())
    all = list(map(int, input().split()))
    ans = 0
    for i in all:
        mom = 1/i
        ans += mom
    dad = 1/ans
    print(dad)
resolve()