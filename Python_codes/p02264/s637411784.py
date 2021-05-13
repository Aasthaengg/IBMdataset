from collections import deque

def doRoundRobin(nt,q):
    result = []

    countTime = 0

    while len(nt) > 0:
        tmp = nt.popleft()
        if tmp[1] <= q:
            countTime += tmp[1]
            result.append([tmp[0],countTime])
        else:
            tmp[1] -= q
            countTime += q
            nt.append(tmp)
    return result


if __name__ == '__main__':
    n, q = map(int,input().split())
    
    nameTime = deque()
    for _ in range(n):
        a, b =  input().split()
        nameTime.append([a,(int)(b)])

    resultNameTime = doRoundRobin(nameTime,q)

    for x in resultNameTime:
        print(x[0],x[1])