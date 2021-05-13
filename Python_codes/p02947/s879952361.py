def main():
    n = int(input())
    slis = list()
    ans = 0
    sdic = {}
    for _ in range(n):
        s = input()
        s = ''.join(sorted(s))
        #print(s)
        if s in sdic:
            tmp = sdic[s]
            ans += tmp
            sdic[s] += 1
        else:
            sdic[s] = 1
            #print(sdic)
    print(ans)

    


if __name__ == "__main__":
    main()
