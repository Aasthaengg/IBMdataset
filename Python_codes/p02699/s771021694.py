print("unsafe" if (lambda s, w: s <= w)(*map(int, input().split())) else "safe")
