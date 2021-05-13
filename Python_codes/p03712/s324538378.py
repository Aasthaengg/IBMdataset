def main():
    H, W = map(int, input().split())
    grid = []
    grid.append(['#']*(W+2))
    for _ in range(H):
        grid.append(['#'] + list(input()) + ['#'])
    grid.append(['#']*(W+2))
    
    for g in grid:
        print(''.join(g))

if __name__ == "__main__":
    main()
