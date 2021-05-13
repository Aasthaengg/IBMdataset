def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n, m = map(int, input().split())
    from bisect import insort_left as il
    pref = [[] for _ in range(n)]
    for i in range(m):
        p, y = map(int, input().split())
        p -= 1
        il(pref[p], (y, i))
    
    def tostr(x):
        return '0'*(6-len(str(x+1)))+str(x+1)

    ans = [0]*m    
    for i in range(n):
        x = pref[i]
        for j in range(len(x)):
            ans[x[j][1]] = tostr(i)+tostr(j)
    
    for x in ans:
        print(x)

    
if __name__ == '__main__':
    main()