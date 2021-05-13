if __name__ == "__main__":
    ct = 0
    while True:
        nums = map( int, raw_input().split())
        H = nums[0]
        W = nums[1]
        if H == 0:
            if W == 0:
                break

        sf = ""
        sb = ""
        j = 0
        while j < W:
            if j == 0:
                sb += "#"
            elif j == W-1:
                sb += "#"
            else:
                sb += "."
            sf += "#"
            j += 1

        i = 0
        while i < H:
            if i == 0:
                print sf
            elif i == H-1:
                print sf
            else:
                print sb
            i += 1
        print