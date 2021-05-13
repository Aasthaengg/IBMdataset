def main():
    s = input()
    k = int(input())
    l = set()
    ls = len(s)
    clist = sorted(list(set(list(s))))
    ladd = l.add
    for i in clist:
        x = []
        for j in range(ls):
            if i == s[j]:
                x.append(j)
        ladd(i)
        for j in range(len(x)):
            idx = x[j]
            xxx = s[idx]
            c = 0
            for t in range(idx+1,ls):
                xxx = xxx +s[t]
                ladd(xxx)
                c += 1
                if c > k:
                    break
        if len(l) >= k:
            l = list(l)
            print(sorted(l)[k-1])
            break
    
if __name__ == '__main__':
    main()