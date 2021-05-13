import sys
def main():
    input = sys.stdin.readline
    N=int(input())
    AB=[tuple(map(int, input().split())) for _ in range(N)]
    scoresA = [(a+b,a,i) for i,(a,b) in enumerate(AB)]
    scoresB = [(b+a,b,i) for i,(a,b) in enumerate(AB)]
    scoresA.sort(reverse=True)
    scoresB.sort(reverse=True)
    ans=0
    used=[False]*N
    ai=bi=0
    for i in range(N):
        if i&1:
            while used[scoresB[bi][2]]: bi+=1
            ans-=scoresB[bi][1]
            used[scoresB[bi][2]]=True
        else:
            while used[scoresA[ai][2]]: ai+=1
            ans+=scoresA[ai][1]
            used[scoresA[ai][2]]=True
    print(ans)

if __name__ == '__main__':
    main()