from collections import defaultdict
def main():
    def fcalc(cl,c):
        f = 0
        for i in cl.keys():
            if i != c:
                f += d[i-1][c-1]*cl[i]
        return f
                
    n,c = map(int,input().split())
    d = [list(map(int,input().split())) for _ in range(c)]
    color = [list(map(int,input().split())) for _ in range(n)]
    clist = [defaultdict(int),defaultdict(int),defaultdict(int)]
    for i in range(n):
        for j in range(n):
            clist[(i+j+2)%3][color[i][j]] += 1
    ans_list = []
    for i in range(1,c+1):
        f1 = fcalc(clist[0],i)
        for j in range(1,c+1):
            if i != j:
                f2 = fcalc(clist[1],j)
                for k in range(1,c+1):
                    if j != k and k != i:
                        f3 = fcalc(clist[2],k)
                        ans_list.append(f1+f2+f3)
    print(min(ans_list))
    
if __name__ == '__main__':
    main()