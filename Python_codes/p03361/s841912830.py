def main():
    h, w = map(int, input().split())
    inlis = list()
    for _ in range(h):
        alis = list(input())
        inlis.append(alis)
    
    for i in range(h):
        for j in range(w):
            if inlis[i][j] == "#":
                tmp = 0
                if i+1 < h:
                    if inlis[i+1][j] != "#":
                        tmp += 1
                else:
                    tmp += 1
                if j+1 < w:
                    if inlis[i][j+1] != "#":
                        tmp += 1
                else:
                    tmp += 1
                if j-1 >= 0:
                    if  inlis[i][j-1] != "#":
                        tmp += 1
                else:
                    tmp += 1
                if i-1 >= 0:
                    if inlis[i-1][j] != "#":
                        tmp += 1
                else:
                    tmp += 1
                       
                if tmp == 4:
                    print("No")
                    exit()
    print('Yes')
        




if __name__ == "__main__":
    main()