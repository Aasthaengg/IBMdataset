import sys
def input(): return sys.stdin.readline().strip()

def main():
    N = int(input())
    t, a = map(int, input().split())
    for _ in range(N - 1):
        nt, na = map(int, input().split())
        if t * na == a * nt: continue
        # ceilで不動小数点誤差が出てWAになるケースは初めて！
        # C++と同じ流儀で繰り上げしないとダメなんだ。。。
        k = max((t + nt - 1) // nt, (a + na - 1) // na)
        t, a = nt * k, na * k

    print(t + a)




if __name__ == "__main__":
    main()
