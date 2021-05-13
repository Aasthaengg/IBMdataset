# 問題：https://atcoder.jp/contests/abc139/tasks/abc139_a

def main():
    S = input()
    T = input()
    res = 0
    for i in range(3):
        if S[i] == T[i]:
            res += 1
    print(res)

if __name__ == '__main__':
    main()

