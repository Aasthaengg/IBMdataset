def check_inner( W, H, x, y, r):
    if (x-r) < 0:
        return False
    if (x+r) > W:
        return False
    if (y-r) < 0:
        return False
    if (y+r) > H:
        return False
    return True

if __name__ == "__main__":

    nums = map( int, raw_input().split())
    if check_inner( nums[0], nums[1], nums[2], nums[3], nums[4]):
        print "Yes"
    else:
        print "No"