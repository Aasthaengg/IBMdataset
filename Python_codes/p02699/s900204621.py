S,W = input().split()

if 0 <= int(S) <= 100 and 0 <= int(W) <= 100:
    if int(S) <= int(W):
        print("unsafe")
    else:
        print("safe")