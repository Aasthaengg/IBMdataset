def resolve():
    import sys
    from operator import itemgetter
    
    readline = sys.stdin.readline    # 1行だけ文字列にする

    N, M = map(int, readline().split())
    AB = [list(map(int, readline().split())) for _ in [0] * M]
    AB.sort(key=itemgetter(1))
    islands = -float('inf')
    ans = 0
    for left, right in AB:
        if islands <= left:
            ans += 1
            islands = right
    print(ans)
    

if __name__ == "__main__":
    resolve()
