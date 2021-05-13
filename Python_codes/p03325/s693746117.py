# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    n = int(input().rstrip())
    a_list = [int(x) for x in input().rstrip().split(" ")]

    ans = 0
    for a in a_list:
        while a % 2 == 0:
            ans += 1
            a = a // 2

    print(ans)

if __name__ == "__main__":
    resolve()
