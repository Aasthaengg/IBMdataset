import sys
def main():
    input = sys.stdin.readline
    def inputs():
        return (int(x) for x in input().split())
    N,M = inputs()
    E={i:[] for i in range(1,N+1)}
    for i in range(M):
        L,R,D = inputs()
        E[L].append((R,D))
        E[R].append((L,-D))
    visited = {i: False for i in range(1,N+1)}
    dis = [0]*(N+1)
    for i in range(1,N+1):
        if not visited[i]:
            stk = [( i, -1, 0)]
            while stk:
                v, p, d = stk.pop()
                #print(v,p)
                if visited[v]:
                    if dis[v]!=dis[p]+d:
                        print("No")
                        exit()
                    continue
                visited[v] = True
                dis[v]=dis[p]+d
                for u,d in E[v]:
                    if u != p:
                        stk.append((u,v,d))
    print("Yes")
main()