def resolve():
    import math
    N = int(input())
    ans = []
    for i in range(1, math.floor(math.sqrt(N))+1):
        if N%i == 0:
            ans.append(i+N//i-2)
    print(min(ans))
resolve()