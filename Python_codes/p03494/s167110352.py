
def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    n = int(input().rstrip())
    a_list = [int(x) for x in input().rstrip().split(" ")]

    def get_num(num, max_count):
        count = 0
        while num % 2 == 0 and count < max_count:
            num = num // 2
            count += 1
        return count

    first = True
    ans = float('inf')
    for a in a_list:
        count = get_num(a, ans)
        if ans > count:
            ans = count

    print(ans)


if __name__ == "__main__":
    resolve()
