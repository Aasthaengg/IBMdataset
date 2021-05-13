
def Bellman_Ford(node_num:int,start:int,goal:int,VWC:list)->list:
    Ans = [float("inf")]*(node_num + 1)
    node = start
    Ans[start] = 0        
    for _ in range(node_num-1):
        for v,w,c in VWC:
            Ans[w] = min(Ans[w], Ans[v] + c)
    Pre = list(Ans)
    for _ in range(node_num-1):
        for v,w,c in VWC:
            Ans[w] = min(Ans[w], Ans[v] + c)
    if Ans[goal] == Pre[goal]:
        return Ans[goal]
    else:
        return float("inf")
def main():
    N,M = map(int,input().split())
    ABC = [list(map(int,input().split())) for _ in  range(M)]
    newABC = [[a,b,-c] for a,b,c in ABC]
    ans = Bellman_Ford(N,1,N,newABC)
    print(-ans if ans < float("inf") else "inf")
    return


if __name__ == "__main__":
    main()