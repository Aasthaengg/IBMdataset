def main():
    n = int(input())
    lim = {}
    for i in range(n):
        a,b = map(int,input().split())
        if b not in lim.keys():
            lim[b] = [a]
        else:
            lim[b].append(a)
    time = 0
    for k in sorted(lim.keys()):
        time += sum(lim[k])
        if time<=k:
            continue
        else:
            print('No')
            return
    print('Yes')

if __name__ == "__main__":
    main()
