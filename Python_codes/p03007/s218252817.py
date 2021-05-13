def solve():
    N = int(input())
    A = list(map(int,input().split()))
    neg = []
    pos = []
    for a in A:
        if a < 0:
            neg.append(a)
        else:
            pos.append(a)
    
    neg.sort()
    pos.sort()
    
    op = []
    if len(neg) == N:
        pos.append(neg[-1])
        neg.pop()
    
    if len(pos) == N:
        neg.append(pos[0])
        pos = pos[1:]
    
    for i in range(len(pos)-1):
        op.append("{0} {1}".format(neg[0], pos[i]))
        neg[0] -= pos[i]
    
    for ne in neg:
        op.append("{0} {1}".format(pos[-1], ne))
        pos[-1] -= ne
    
    printAns(pos[-1], op)

def printAns(M, op):
    print(M)
    print(*op, sep='\n')
    
if __name__ == '__main__':
    solve()