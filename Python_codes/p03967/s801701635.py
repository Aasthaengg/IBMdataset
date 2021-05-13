def solve():
    S = input()
    even = S[0::2]
    odd = S[1::2]
    ans = odd.count('g')-even.count('p')
    return ans
print(solve())