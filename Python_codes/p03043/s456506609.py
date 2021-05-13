import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    # 等間隔のダイスとコインなので、dの目ごとの勝利確率をだし、平均すると答。
    n, k = map(int, input().split())

    pro = 0
    for i1 in range(1, n + 1):
        if i1 >= k:
            pro += 1
        else:
            pro_t = 1
            while i1 < k:
                pro_t /= 2
                i1 *= 2
            pro += pro_t
    r = pro / n
    print(r)

if __name__ == '__main__':
    main()
