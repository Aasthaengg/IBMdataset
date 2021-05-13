def main():
    a,b = map(int,input().split())
    print(100,100)
    white = [["."]*50 for _ in range(100)]
    black = [["#"]*50 for _ in range(100)]
    a1,b1 = a-1,b-1
    x,y = 0,0
    for i in range(b1//25):
        for j in range(25):
            white[i*2][j*2] = "#"
        x = i+1
    for i in range(b1%25):
        white[x*2][i*2] = "#"
    for i in range(a1//25):
        for j in range(25):
            black[i*2][49-j*2] = "."
        y = i+1
    for i in range(a1%25):
        black[y*2][49-i*2] = "."
    for i,j in zip(white,black):
        print("".join(i) + "".join(j))
    
if __name__ == '__main__':
    main()