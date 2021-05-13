def solve():
    def beat(hp, memo):
        if hp in memo:
            return memo[hp]
        if hp == 1:
            return 1
        else:
            child_hp = hp // 2
            cnt = 1 + beat(child_hp, memo) + beat(child_hp, memo)
            memo[hp] = cnt
            return cnt

    H = int(input())
    print(beat(H, {}))

if __name__ == "__main__":
    solve()