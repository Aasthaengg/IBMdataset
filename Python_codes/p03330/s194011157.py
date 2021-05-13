import itertools



def resolve():
    N,C=map(int,input().split())
    cost=[[int(i) for i in input().split()] for j in range(C)]
    count=[[0 for i in range(C)] for i in range(3)]
    grid=[[int(i)-1 for i in input().split()] for j in range(N)]
    for i in range(N):
        for j in range(N):
            count[(i+j)%3][grid[i][j]]+=1
    seq=list(range(C))
    mx=2**29
    for i in itertools.permutations(seq,3):
        temp=0
        temp+=sum([cost[j][i[0]]*count[0][j] for j in range(C)])
        temp+=sum([cost[j][i[1]]*count[1][j] for j in range(C)])
        temp+=sum([cost[j][i[2]]*count[2][j] for j in range(C)])
        mx=min(mx,temp)
    print(mx)

if __name__ == "__main__":
    resolve()