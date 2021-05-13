#atcoder -take a rest-(easy)

def main():
    N,K = map(int,input().split())
    que = []
    que_x =  []
    que_y = []
    for i in range(N):
        x,y = map(int,input().split())
        que_x.append(x)
        que_y.append(y)
        que.append((x,y))
    que_x.sort()
    que_y.sort()
    ans = 10**100
    for i in range(N):
        for j in range(i,N):
            for _i in range(N):
                for _j in range(_i,N):
                    h,w = que_x[j]-que_x[i],que_y[_j] -que_y[_i]
                    cnt = 0
                    for x,y in que:
                        if que_x[i]<=x<=que_x[j] and que_y[_i]<=y<=que_y[_j]:
                            cnt += 1
                    if cnt >=K:
                        ans = min(ans,h*w)
    print(ans)
    return




if __name__ == "__main__":
    main()


