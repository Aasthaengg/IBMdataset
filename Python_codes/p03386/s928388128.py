# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()
import math

def resolve():
    import sys
    input = sys.stdin.readline
    a, b, k = [int(x) for x in input().rstrip().split(" ")]

    if (b - a + 1)  <= k * 2:
        print("\n".join([str(num) for num in range(a, b+1)]))
    else:
        print("\n".join([str(num) for num in range(a, a+k)]))
        print("\n".join([str(num) for num in range(b-k+1, b+1)]))



if __name__ == "__main__":
    resolve()
