def a_ddcc_finals():
    X, Y = [int(i) for i in input().split()]
    prizes = {1: 300000, 2: 200000, 3: 100000}
    ans = 0
    for rank in (X, Y):
        if rank in prizes.keys():
            ans += prizes[rank]
    ans += 400000 if X == 1 and Y == 1 else 0
    return ans

print(a_ddcc_finals())