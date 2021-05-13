def solve():
    S = input()
    ans = S.count('BW')+S.count('WB')
    return ans
print(solve())