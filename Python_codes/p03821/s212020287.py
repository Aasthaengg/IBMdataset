#67 A - Multiple Array
N = int(input())
A, B = [],[]
for _ in range(N):
    a,b= map(int,input().split())
    A.append(a); B.append(b)
A = list(reversed(A))
B = list(reversed(B))

c = 0
for a,b in zip(A,B):
    # 前に押されたボタンの回数分足される
    a += c
    # ボタンを押さなくてもいい時
    if a%b == 0:
        continue
    # c 回ボタンを押せば Ai は Bi の倍数になる
    c += b-(a%b)
print(c)