from sys import stdin

def getval():
    n,m = map(int,input().split())
    h = list(map(int,stdin.readline().split()))
    p = [list(map(int,stdin.readline().split())) for i in [0]*m]
    return n,m,h,p

def main(n,m,h,p):
    g = [[] for i in range(n)]
    for i in p:
        g[i[0]-1].append(i[1]-1)
        g[i[1]-1].append(i[0]-1)
    ans = 0
    for i in range(n):
        if not g[i]:
            ans += 1
        else:
            temp = h[i]
            flag = True
            for j in g[i]:
                if h[j]>=temp:
                    flag = False
                    break
            if flag:
                ans += 1
    print(ans)
                

if __name__=="__main__":
    n,m,h,p = getval()
    main(n,m,h,p)