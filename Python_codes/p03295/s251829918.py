def IslandsWar():
    n, m = map(int, input().split())
    a = [list(map(int,input().split())) for _ in range(m)]
    a.sort(key=lambda x: x[1])
    removes = [a[0][1]]

    for i, j in a[1:]:
        check = False
        for k in removes:
            if i < k:
                check = True
                break
        if not check:
            removes.append(j)
    print(len(removes))
            
if __name__ == "__main__":
    IslandsWar()
