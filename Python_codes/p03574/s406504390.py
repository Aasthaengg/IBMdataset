if __name__ == "__main__":
    h,w = map(int,input().split())
    s = []
    s.append([0]*(w+2))

    for i in range(h):
        q = [0]
        q.extend(list(input()))
        q.append(0)
        s.append(q)
    s.append([0]*(w+2))

    for p in range(h):
        for q in range(w):
            if s[p+1][q+1] == "#":
                print("#",end = "")
            else:
                aro = [s[p][q],s[p+1][q],s[p+2][q],s[p][q+1],s[p+2][q+1],s[p][q+2],s[p+1][q+2],s[p+2][q+2]]
                print(aro.count("#"),end = "")
        print("")