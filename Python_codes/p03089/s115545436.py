def main():
    n = int(input())
    b = list(map(int, input().split()))
    f = True
    ans = []
    while len(b) > 0:
        sf = True
        for i in reversed(range(len(b))):
            if b[i] == i+1:
                b.pop(i)
                ans.append(i+1)
                sf = False
                break
        if sf:
            f = False
            break
    if f:
        for v in reversed(ans):
            print(v)
    else:
        print("-1")

if __name__ == "__main__":
    main()