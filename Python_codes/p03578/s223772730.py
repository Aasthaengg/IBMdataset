def main():
    n = int(input())
    ddic = {}
    tlis = []
    dlis = list(map(int, input().split()))
    m = int(input())
    tlis = list(map(int, input().split()))
    for d in dlis:
        if d in ddic:
            ddic[d] += 1
        else:
            ddic[d] = 0
    for t in tlis:
        if t in ddic and ddic[t] >= 0:
            #print(t,tlis, dlis)
            ddic[t] -= 1
        else:
            #print(t,tlis, dlis)
            print("NO")
            exit()
    print("YES")


if __name__ == "__main__":
    main()