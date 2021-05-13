def main():
    N,M = map(int, input().split())
    req = [[0,0] for i in range(M)]
    for i in range(M):
        a,b = map(lambda x:x-1, map(int, input().split()))
        req[i] = [b,a]
    # bの昇順にソートして小さいbから叶えていく
    req = sorted(req)
    ans = 1
    pos = req[0][0]-1
    for i in range(1,M):
        b,a = req[i]
        if pos<a:
            # できるだけ右の橋を取り除く
            ans += 1
            pos = b-1
    print(ans)

main()
