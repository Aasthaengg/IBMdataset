from itertools import combinations

def getval():
    n = int(input())
    f = [list(map(int,input().split())) for i in range(n)]
    p = [list(map(int,input().split())) for i in range(n)]
    return n,f,p

def main(n,f,p):
    ans = 0
    for i in range(n):
        temp = 0
        for j in f[i]:
            temp += j
        ans += p[i][temp]

    for i in range(1,10):
        for c in combinations(range(10),i):
            pro = 0
            for j in range(n):
                temp = 0
                for k in c:
                    temp += f[j][k]
                pro += p[j][temp]
            ans = max(ans,pro)

    print(ans)

if __name__=="__main__":
    n,f,p = getval()
    main(n,f,p)