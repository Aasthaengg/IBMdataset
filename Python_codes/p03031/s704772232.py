def main():
    N,M = map(int,input().split())
    switches = []
    for i in range(M):
        switches.append(list(map(int,input().split()))[1:])
    P = list(map(int,input().split()))
    ans = 0
    for i in range(2**N):
        on = [False]*N
        for j in range(N):
            if (2**j) & i :
                on[j] = True

        for j in range(M):
            count = 0
            for s in switches[j]:
                if on[s-1]:
                    count += 1
            if count % 2 != P[j]:
                break
            else:
                continue
            break
        else:
            ans += 1
    print(ans)










main()