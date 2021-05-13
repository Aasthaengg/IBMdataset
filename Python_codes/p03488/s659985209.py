def main():
    import sys
    input = sys.stdin.readline

    s = input().rstrip()
    x,y = map(int, input().split())
    f = s.split('T')
    dx_list = list(map(len, f[::2]))
    dy_list = list(map(len, f[1::2]))
    
    nx = dx_list.pop(0)
    ny = 0

    dx_list.sort(reverse=True)
    dy_list.sort(reverse=True)

    for dx in dx_list:
        if x >= nx:
            nx += dx
        else:
            nx -= dx
    for dy in dy_list:
        if y >= ny:
            ny += dy
        else:
            ny -= dy

    if nx == x and ny == y:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()