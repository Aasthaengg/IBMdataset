def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = set()
    # 逆順で考える
    # indexではなく数値で考える
    for i in reversed(range(1, n+1)):
        # 倍数計算は2倍したあとは数値的にnまでiごとにという形で算出
        for j in range(i*2, n+1, i):
            a[i-1] ^= a[j-1]
        if a[i-1] == 1:
            ans.add(i)
    print(len(ans))
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()