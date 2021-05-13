def getLuca(n):
    memo = [2, 1]

    for i in range(2, n+1):
        memo.append(memo[i-1] + memo[i-2])
    
    return memo[n]

def resolve():
    N = int(input())
    print(getLuca(N))
    return

resolve()