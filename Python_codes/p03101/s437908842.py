#!/usr/bin/env python3

def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    all_cells = H * W
    black_cells = h * W + w * H - (h * w)
    print(all_cells - black_cells)

if __name__ == "__main__":
    main()
