import sys
input = sys.stdin.readline
def main():
    N,M = map(int,input().split())
    pos = [0 for _ in range(N)]
    for i in range(M):
        a,b = map(int,input().split())
        pos[a-1] += 1
        pos[b-1] += 1

    for i in range(N):
        if pos[i]%2 != 0:
            print("NO")
            exit()

    print("YES")

if __name__ == "__main__":
    main()