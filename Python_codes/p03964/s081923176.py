import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    X = [list(map(int,input().split())) for _ in range(N)]
    na,nb = X[0][0],X[0][1]
    for i in range(N-1):
        i += 1
        x,y = X[i][0],X[i][1]
        if (x >= na and y >= nb):
            na,nb = x,y
        elif (x < na and y >= nb):
            q = -(-na//x)
            na,nb = x*q,y*q
        elif (x >= na and y < nb):
            q = -(-nb//y)
            na,nb = x*q,y*q
        else:
            use = max(-(-na//x),-(-nb//y))
            na,nb = x*use,y*use
    
    print(na+nb)
    
if __name__ == "__main__":
    main()