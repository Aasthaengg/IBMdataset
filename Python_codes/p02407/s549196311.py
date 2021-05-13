if __name__ == "__main__":
    n = int(raw_input())

    nums = map( int, raw_input().split())
    nlen = len( nums )
    nlast = n - 1
    i = nlast
    while i >= 0:
        if i == 0:
            print nums[i]
        else:
            print nums[i],
        i = i - 1