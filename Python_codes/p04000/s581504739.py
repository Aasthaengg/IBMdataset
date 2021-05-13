import sys
def input(): return sys.stdin.readline().strip()

def main():
    """
    https://atcoder.jp/contests/abc045/submissions/14945636
    が高速に動作していたので参考に写経する。

    各黒マスに対して、それを含むテンプレートを左上の座標値で管理する。
    （写経元は右下座標で管理してる）
    このテンプレート及びそこに黒マスが何個入っているかを管理しておけば
    黒マス位置をソートして全体位置を把握していなくてもオンラインで更新が可能。
    """
    H, W, N = map(int, input().split())
    ans = [0] * 10
    templates = {}
    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(9):
            # (h, w)がテンプレートの左上座標
            h, w = (a - 3) + i // 3, (b - 3) + i % 3
            if h < 0 or w < 0: continue
            if h > H - 3 or w > W - 3: continue
            idx = h * W + w
            if idx in templates:
                ans[templates[idx]] -= 1
                templates[idx] += 1
                ans[templates[idx]] += 1
            else:
                templates[idx] = 1
                ans[1] += 1
    ans[0] = (H - 2) * (W - 2) - sum(ans[1:])
    for a in ans: print(a)


if __name__ == "__main__":
    main()
