N, A, B = map(int, input().split())
x = B - A
if x % 2 == 0:
    print(x//2)
else:
    # 左に持って行って寄せる
    l = (A-1) + 1 + (B-A-1)//2
    # 右に持って行って寄せる
    r = (N-B) + 1 + (B-A-1)//2
    print(min(r, l))
