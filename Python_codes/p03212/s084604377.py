import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())

def main():
    n = II()
    def dfs(cur, use):
        counter = 0
        def dfs_(cur, use):
            nonlocal counter
            if cur > n:      return None
            if use == 0b111: counter += 1
            dfs_(cur*10 + 7, use | 0b001)
            dfs_(cur*10 + 5, use | 0b010)
            dfs_(cur*10 + 3, use | 0b100)
        dfs_(cur, use)
        return counter
    print(dfs(0, 0))

if __name__ == '__main__':
    main()