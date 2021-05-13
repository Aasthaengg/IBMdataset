import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    row = [int(x) for x in input().rstrip().split(" ")]

    a = row[0]
    b = row[1]
    c = row[2]

    count = 0
    while(a%2==0 and b%2==0 and c%2==0):
        if(a==b and b==c):
            count = -1
            break
        count += 1
        tmpa = b//2 + c//2
        tmpb = a//2 + c//2
        tmpc = b//2 + a//2

        a = tmpa
        b = tmpb
        c = tmpc

    print(count)

if __name__ == "__main__":
    resolve()
