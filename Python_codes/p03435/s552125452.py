import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    c = []
    for _ in range(3):
        c.append(tuple(map(int, input().split())))
    for i1 in range(101):
        for i2 in range(101):
            if i1 - c[0][0] == i2 - c[0][1]:
                i3 = c[0][2] - (c[0][0] - i1)
                if i1 - c[1][0] == i2 - c[1][1] == i3 - c[1][2]:
                    if i1 - c[2][0] ==i2 -c[2][1] == i3 - c[2][2]:
                        print('Yes')
                        sys.exit()
    print('No')
if __name__ == '__main__':
    main()