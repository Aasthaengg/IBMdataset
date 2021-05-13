def resolve():
    N = int(input())
    pow = list(map(int, input().split()))
    ans = []
    for i in range(N):
        for j in range(N):
            if i != j:
                ans.append(pow[i]*pow[j])
    print((sum(ans))//2)
resolve()