def resolve(S: int, W: int) -> str:
    if S <= W:
        return 'unsafe'
    else:
        return 'safe'

if __name__ == '__main__':
    S, W = map(int, input().split())
    res = resolve(S, W)
    print(res)
