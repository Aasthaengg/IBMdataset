def main():
    W,H,x,y = [int(x) for x in input().split()]
    area = W*H/2
    if x == W/2 and y == H/2:
        print(area,1)
    else:
        print(area,0)

if __name__ == '__main__':
    main()