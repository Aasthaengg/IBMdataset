import sys
import math
def main():
    for line in sys.stdin:
        n = int(line)
        if n == 0:
            break
        else:
            A = list(map(float, input().split()))
            t1 = 0
            for a in A:
                t1 += a
            ave = t1 / len(A)
            
            t2 = 0
            for a in A:
                t2 += (a - ave) ** 2
            s = math.sqrt(t2 / n)
            print(s)


if __name__ == "__main__":
    main()