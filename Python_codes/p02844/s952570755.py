def getval():
    n = int(input())
    s = input()
    return n,s 

def main(n,s):
    pos = [-1 for i in range(10)]
    for i in range(n):
        temp = int(s[i])
        if pos[temp]==-1:
            pos[temp] = i 
    flag1 = [[[False for i in range(10)] for i in range(10)] for i in range(10)]
    flag2 = [[False for i in range(10)] for i in range(10)]
    for i in range(10):
        if pos[i]==-1 or pos[i]>=n-1:
            continue
        for j in range(pos[i]+1,n):
            f = flag2[i]
            temp = int(s[j])
            for k in range(10):
                if f[k]:
                    flag1[i][k][temp] = True 
            if not f[temp]:
                flag2[i][temp] = True
    ans = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if flag1[i][j][k]:
                    ans += 1
    print(ans)

if __name__=="__main__":
    n,s = getval()
    main(n,s)