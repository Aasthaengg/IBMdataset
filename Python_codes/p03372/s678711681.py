from bisect import bisect_left
def main():
    n,c = map(int,input().split())
    xv = [tuple(map(int,input().split())) for _ in range(n)]
    xvr = []
    for i in range(n):
        j = n-i-1
        xvr.append((c-xv[j][0],xv[j][1]))
    xvv = [0]*n
    xvv[0] = xv[0]
    for i in range(1,n):
        xvv[i] = (xv[i][0],xvv[i-1][1]+xv[i][1])
    xvrv = [0]*n
    xvrv[0] = xvr[0]
    for i in range(1,n):
        xvrv[i] = (xvr[i][0],xvrv[i-1][1]+xvr[i][1])
    xvm = [(0,0)]
    xvmi = [0]
    for i in xvv:
        j = xvm[-1]
        if i[1]-i[0] >= j[1]-j[0]:
            xvm.append(tuple(i))
            xvmi.append(i[0])
    xvrm = [(0,0)]
    xvrmi = [0]
    for i in xvrv:
        j = xvrm[-1]
        if i[1]-i[0] >= j[1]-j[0]:
            xvrm.append(tuple(i))
            xvrmi.append(i[0])
    ans = max([xvm[-1][1]-xvm[-1][0],xvrm[-1][1]-xvrm[-1][0]])
    for i in xvm:
        t = c-i[0]
        idx = bisect_left(xvrmi,t)-1
        tans = xvrm[idx][1]-xvrm[idx][0]+i[1]-i[0]*2
        if tans > ans:
            ans = tans
    for i in xvrm:
        t = c-i[0]
        idx = bisect_left(xvmi,t)-1
        tans = xvm[idx][1]-xvm[idx][0]+i[1]-i[0]*2
        if tans > ans:
            ans = tans
    print(ans)
    
if __name__ == '__main__':
    main()