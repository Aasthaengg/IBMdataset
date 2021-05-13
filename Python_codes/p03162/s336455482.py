def getval():
    n = int(input())
    h = [list(map(int,input().split())) for i in range(n)]
    return n,h

def main(n,h):
    dp = [[h[0][0],h[0][1],h[0][2]]]
    for i in range(1,n):
        cur = h[i]
        prev = dp[-1]
        temp = []
        temp.append(max(prev[1],prev[2])+cur[0])
        temp.append(max(prev[0],prev[2])+cur[1])
        temp.append(max(prev[0],prev[1])+cur[2])
        dp.append(temp)
    print(max(dp[-1]))
    
if __name__=="__main__":
    n,h = getval()
    main(n,h)
