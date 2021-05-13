def test():
    r = int(input())
    rank = {1199:"ABC",2799:"ARC",4200:"AGC"}

    if r < 1200:
        print(rank[1199])
    elif r >= 1200 and r < 2800:
        print(rank[2799])
    else:
        print(rank[4200]) 


if __name__ == "__main__":
    test()
