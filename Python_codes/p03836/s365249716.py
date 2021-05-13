def main():
    sx, sy, tx, ty = list(map(int, input().split()))
    dx = tx - sx
    dy = ty - sy
    ans = []
    ans.append(''.join(['D', 'R' * (dx + 1), 'U' * (dy + 1), 'L']))
    ans.append(''.join(['D' * dy, 'L' * dx]))
    ans.append(''.join(['U', 'R' * (dx - 1), 'U' * (dy - 1), 'R']))
    ans.append(''.join(['U', 'L' * 2, 'D' * (dy - 1), 'L' * (dx - 1), 'D' * 2, 'R']))
    print(''.join(ans))



if __name__ == '__main__':
    main()
