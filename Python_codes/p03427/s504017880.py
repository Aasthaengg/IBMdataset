# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    num_list = [int(x) for x in input().rstrip()]

    ans = sum(num_list)

    for i in range(1, len(num_list)+1):
        tmp = sum([x for x in num_list[:i]]) - 1 + 9 * (len(num_list) - i)
        if tmp > ans:
            ans = tmp

    print(ans)


if __name__ == "__main__":
    resolve()
