def main():
    x, y = map(int, input().split())
    if x <= y:
        if x == 0 or y == 0:
            print(y-x)
        elif 0 < x and 0 < y:
            print(y-x)
        elif x < 0 and y < 0:
            print(y-x)
        else:
            if -x <= y:
                print(y-(-x)+1)
            else:
                print((-x)-y+1)
    else:
        if x == 0 or y == 0:
            print(x-y+1)
        elif 0 < x and 0 < y:
            print(x-y+2)
        elif x < 0 and y < 0:
            print(min(x-y+2, (-y)-x+1))
        else:
            if x <= -y:
                print((-y)-x+1)
            else:
                print(y-(-x)+1)

if __name__ == "__main__":
    main()