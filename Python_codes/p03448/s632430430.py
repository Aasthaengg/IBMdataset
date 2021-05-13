
def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    a = int(input().rstrip())
    b = int(input().rstrip())
    c = int(input().rstrip())
    x = int(input().rstrip())

    ans = 0
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if (i*500+j*100+k*50) == x:
                    ans += 1
    print(ans)




if __name__ == "__main__":
    resolve()
