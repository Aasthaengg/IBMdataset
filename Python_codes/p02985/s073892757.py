def main():
    from collections import defaultdict, deque
    import sys
    mod = 10**9+7
    N, K = map(int, input().split())
    dic= defaultdict(list)

    for i in range(N-1):
        a, b =  map(int, input().split())
        dic[a].append(b)
        dic[b].append(a)

    seen = [-1]*N
    seen[0]=0
    ans = K
    
    for i in range(len(dic[1])):
        if K-i-1<=0:
            print(0)
            sys.exit()
        ans *= K-i-1
        ans %= mod

    queue = deque(dic[1])
    for  p in dic[1]:
        seen[p-1]=0

    while queue:
        bla= queue.popleft()
        for j in range(len(dic[bla])-1):
            if K-j-2<=0:
                print(0)
                sys.exit()
            ans *= K-j-2
            ans %= mod

        for i in dic[bla]:
            if len(dic[i])==1:
                continue
            if seen[i-1]==-1:
                queue.append(i)
                seen[i-1]=0
    print(ans)
main()