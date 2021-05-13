if __name__ == "__main__":
    N,H,W = map(int,input().split())
    A = []
    B = []
    counter = 0
    for i in range(N):
        a,b = map(int,input().split())
        if(a >= H and b >= W):
            counter += 1
    print(counter)
