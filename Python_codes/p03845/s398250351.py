# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline
    n = int(input().rstrip())
    ts = [int(x) for x in input().rstrip().split(" ")]
    original_time = sum(ts)
    m = int(input().rstrip())
    for i in range(m):
        p, x = [int(x) for x in input().rstrip().split(" ")]
        print(original_time - ts[p-1] + x)

if __name__ == "__main__":
    resolve()
