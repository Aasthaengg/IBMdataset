# abc174_c.py
# https://atcoder.jp/contests/abc174/tasks/abc174_c


# [開発時用] ログ関数
def lg(value):
    flag = False
    flag = True
    if flag:
        print(str(value))


# [開発時用] exit処理
def xt(log):
    lg('★exit() - ' + str(log))
    exit()


# 本体
def get_results():

    # 引数処理部
    lines = list()
    # 仕様でn行と決まっている場合(の例)
    lines_count = 1
    # 先頭行のNで行数が決まる場合(の例)
    # line = input()
    # lines.append(line)
    # N = int(line)
    # lines_count = N
    for _ in range(lines_count):
        lines.append(input())

    # 演算部
    # S = lines[0]
    K = int(lines[0])
    # N, M = list(map(int, lines[0].split()))
    # values = list(map(int, lines[0].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    result = 0

    tmp = 7

    if K % 5 == 0 or K % 2 == 0:
        return [-1]

    for k in range(K):

        q, mod = divmod(tmp, K)
        if mod == 0:
            return [k+1]
        tmp = mod * 10 + 7


# 主処理
def main():
    results = get_results()

    for result in results:
        print(result)


# 起動処理
if __name__ == '__main__':
    main()
