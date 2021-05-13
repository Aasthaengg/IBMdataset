
def main():
    H, W, K = map(int, input().split(" "))
    c = [[c for c in input()] for _ in range(H)]
    cnt = 0
    ans = 0
    for i in range(1 << H):
        for j in range(1 << W):
            cnt = 0
            for ii in range(H):
                for jj in range(W):
                    if(i >> ii & 1):
                        continue
                    if(j >> jj & 1):
                        continue
                    if(c[ii][jj] == '#'):
                        cnt += 1
            if cnt == K :
                ans += 1
    print(ans)
    
    

if __name__ == "__main__":
    main()