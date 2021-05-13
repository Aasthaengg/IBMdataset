def main():
    W,H,N = map(int,input().split())
    X = 0 #a=1初期値
    Y = 0 #a=3初期値
    for _ in range(N):
        x,y,a = map(int,input().split())
        if a == 1:
            X = max(X,x)
        elif a == 2:
            W = min(W,x)
        elif a == 3:
            Y = max(Y,y)
        elif a == 4:
            H = min(H,y)
    #Sを求める
    S = max((W-X),0) * max((H-Y),0)
    print(S)
if __name__ == '__main__':
    main()

