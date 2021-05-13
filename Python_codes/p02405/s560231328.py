if __name__ == "__main__":
    ct = 0
    while True:
        nums = map( int, raw_input().split())
        H = nums[0]
        W = nums[1]
        if H == 0:
            if W == 0:
                break

        so = ""
        se = ""
        j = 0
        while j < W:
            if j & 1:
                se += "."
                so += "#"
            else:
                se += "#"
                so += "."
            j += 1

        i = 0
        while i < H:
            if i & 1:
                print so
            else:
                print se
            i += 1
        print