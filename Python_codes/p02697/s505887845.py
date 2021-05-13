import sys
input = sys.stdin.buffer.readline

def main():
    N,M = map(int,input().split())
    cl = []
    for i in range(M//2):
        cl.append((i+1,(M//2)*2+1-i))
    for i in range(-(-M//2)):
        l = (M//2)*2+i+2
        cl.append((l,l+(-(-M//2)-i)*2-1))
    
    for i in range(M):
        print(*cl[i])
    
if __name__ == "__main__":
    main()