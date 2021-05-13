# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()
import math

def resolve():
    import sys
    input = sys.stdin.readline
    a, b = [int(x) for x in input().rstrip().split(" ")]

    for i in range(int(100.0 / 0.08) + 1):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            return
    print(-1)



if __name__ == "__main__":
    resolve()
