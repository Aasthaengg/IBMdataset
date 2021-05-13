def main():
    x1,y1,x2,y2 = map(int,input().split())
    diffx = x2 - x1
    diffy = y2 - y1
    x3 = x2 - diffy
    y3 = y2 + diffx
    x4 = x3 - diffx
    y4 = y3 - diffy
    print(x3,y3,x4,y4)
    
if __name__ == "__main__":
    main()