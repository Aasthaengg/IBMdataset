if __name__ == "__main__":
    N, M = map(int, input().split())
    T = []
    for i in range(M):
        p, y = map(int, input().split())
        T.append((p, y, i))
    T.sort()
    ID = []
    cp = -1
    count = -1
    for p, y, i in T:
        if p != cp:
            cp = p
            count = 1
        ID.append((i, "0"*(6-len(str(cp)))+str(cp)+"0"*(6-len(str(count)))+str(count)))
        count += 1
    ID.sort()
    for i , id in ID:
        print(id)
