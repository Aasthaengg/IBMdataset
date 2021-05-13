def abc049_b():
    H, _ = map(int, input().split())
    C = [str(input()) for _ in range(H)]
    stretch = []
    for ln in C:
        stretch.append(ln)
        stretch.append(ln)
    print(*stretch, sep='\n')

abc049_b()