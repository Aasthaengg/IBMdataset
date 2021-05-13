def main():
    H,W=map(int,input().split())
    m=[input() for _ in range(H)]
    is_ok = True
    for h in range(H):
        for w in range(W):
            if m[h][w] == "#":
                if -1 < h-1 and m[h-1][w] == "#":
                    pass
                elif -1 < w-1 and m[h][w-1] == "#":
                    pass
                elif h+1 < H and m[h+1][w] == "#":
                    pass
                elif w+1 < W and m[h][w+1] == "#":
                    pass
                else:
                    print("No")
                    return
    print("Yes")
        
if __name__ == "__main__":
    main()