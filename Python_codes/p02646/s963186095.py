
def resolve():
    A, V = map(int, input().split())
    B, W = map(int, input().split())
    T = int(input())

    diff_d = abs(A - B)
    dif_move = (V - W) * T

    if diff_d <= dif_move:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    resolve()
