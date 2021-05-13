def solve():
    N,K = map(int,input().split())
    V = list(map(int,input().split()))

    ans = -float('inf')
    for left in range(min(N,K)+1):
        for right in range(min(N,K)-left+1):
            took = V[:left] + V[-1:-(right+1):-1]
            took.sort()
            sm = sum(took)
            for put in range(K-(left+right)):
                if len(took) == put:
                    break
                if took[put] >= 0:
                    break
                sm += abs(took[put])
            
            ans = max(ans,sm)
    
    print(ans)
if __name__ == '__main__':
    solve()