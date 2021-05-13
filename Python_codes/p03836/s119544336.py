# C - Back and Forth
def main():
    sx, sy, tx, ty = map(int, input().split())

    rx = tx - sx
    ry = ty - sy

    ans = []

    # path1
    for _ in range(ry):
        ans.append('U')
    for _ in range(rx):
        ans.append('R')

    # path2
    for _ in range(ry):
        ans.append('D')
    for _ in range(rx):
        ans.append('L')

    # path3
    ans.append('L')
    for _ in range(ry+1):
        ans.append('U')
    for _ in range(rx+1):
        ans.append('R')
    ans.append('D')
    
    # path4
    ans.append('R')
    for _ in range(ry+1):
        ans.append('D')
    for _ in range(rx+1):
        ans.append('L')
    ans.append('U')
    
    print(''.join(ans))


if __name__ ==  "__main__":
    main()