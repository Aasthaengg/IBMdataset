# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()
# row = [int(input().rstrip()) for _ in range(n)]

def resolve():
    import sys
    input = sys.stdin.readline
    n = int(input().rstrip())
    a_list = [int(x) for x in input().rstrip().split(" ")]

    # 奇数になる組み合わせ
    odd = 1
    for a in a_list:
        if a % 2 == 0:
            odd *= 2

    print(3 ** len(a_list) - odd)



if __name__ == "__main__":
    resolve()
