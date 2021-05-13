if __name__ == "__main__":
    nums =map( int, raw_input().split())
    if nums[0] < nums[1] :
        print "a < b"
    elif nums[0] > nums[1] :
        print "a > b"
    else:
        print "a == b"