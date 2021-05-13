# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    n = input().rstrip()
    a_list = [int(x) for x in input().rstrip().split(" ")]

    print(sum(a_list) - len(a_list))

if __name__ == "__main__":
    resolve()
