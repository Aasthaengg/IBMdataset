if __name__ == '__main__':
    h, w = map(int, input().split())
    maiz = []
    count =[]
    for i in range(h):
        a = input()
        maiz.append(a)
        count.append([0]*w)

    for i in range(h):
        for j in range(w):
            if maiz[i][j] == "#":
                count[i][j] = "#"
                if i > 0 and maiz[i-1][j] == ".":
                    count [i-1][j] +=1
                if i < h -1  and maiz[i+1][j] == ".":
                    count [i+1][j] +=1
                if j > 0 and maiz[i][j-1] == ".":
                    count [i][j-1] +=1
                if j < w -1  and maiz[i][j+1] == ".":
                    count [i][j+1] +=1
                if i > 0 and j > 0 and maiz[i-1][j-1] == ".":
                    count [i-1][j-1] +=1
                if i < h -1 and j < w-1  and maiz[i+1][j+1] == ".":
                    count [i+1][j+1] +=1
                if i > 0 and j < w-1 and maiz[i-1][j+1] == ".":
                    count [i-1][j+1] +=1
                if i < h -1 and j >0  and maiz[i+1][j-1] == ".":
                    count [i+1][j-1] +=1


    for i in count:
        ans = ""
        for j in i :
            ans += str(j)
        print(ans)




