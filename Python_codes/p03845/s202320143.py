# B - Contest with Drinks Easy
def main():
    import copy
    _ = int(input())
    t = list(map(int, input().split()))
    m = int(input())
    px = [input().split() for i in range(m)]
    

    for i in range(m):
        tt = copy.copy(t)
        tt[int(px[i][0])-1] = int(px[i][1])
        print(sum(tt)) 


if __name__ ==  "__main__":
    main()