from itertools import zip_longest

def solve():
    N = input()
    O = input()
    ans = ''
    for x, y in zip_longest(N, O, fillvalue=''):
        ans += x + y
    print(ans)

if __name__ == "__main__":
    solve()