def main():
    n, k = map(int, input().split())
    v = [int(x) for x in input().split()]
    
    ans = 0
    r = min([n, k])
    for i in range(r+1):
        for j in range(r+1-i):
            sub = sum(v[:i])+sum(v[n-j:n])
            minus = []
            for l in range(n):
                if (l < i or n-j < l) and v[l] < 0:
                    minus.append(v[l])
            minus.sort()
            sub -= sum(minus[:min([len(minus), k-i-j])])
            if ans < sub:
                ans = sub
        
    print(ans)

if __name__ == "__main__":
    main()