import sys
def input(): return sys.stdin.readline().strip()
mod = 10**9+7

def main():
    n, m = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    """
    各長方形を１つ１つの矩形に分解することで、もともと線で区切られていた
    最小の長方形たちが個別に何回足されるかを見る。
    長方形が縦に(m-1)個、横に(n-1)個並んでいるとして、(i, j)の位置にある長方形は
        i * (m - i) * j * (n - j)
    回足される。
    これをシグマ計算するとx, y方向独立に解いてよいことがわかる。
    """
    x = 0
    for j in range(1, n):
        coeff = j * (n - j) % mod
        x += coeff * (X[j] - X[j - 1]) % mod
        x %= mod
    y = 0
    for i in range(1, m):
        coeff = i * (m - i) % mod
        y += coeff * (Y[i] - Y[i - 1]) % mod
        y %= mod
    print(x * y % mod)

if __name__ == "__main__":
    main()
