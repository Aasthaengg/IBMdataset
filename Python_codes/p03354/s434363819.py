import sys
input = sys.stdin.buffer.readline

def main():
    N,M = map(int,input().split())
    p = list(map(int,input().split()))
    
    I = [i for i in range(N)]
    def root(x):
        if x == I[x]:
            return x
        I[x] = root(I[x])
        return I[x]

    for _ in range(M):
        x,y = map(int,input().split())
        a = root(x-1)
        b = root(y-1)
        if a != b:
            I[b] = a

    c = 0
    for i in range(N):
        if root(p[i]-1) == root(i):
            c += 1
            
    print(c)
    
if __name__ == "__main__":
    main()
