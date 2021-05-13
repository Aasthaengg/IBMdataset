import sys
input=sys.stdin.readline

def main():
    N,M = map(int, input().split())
    A = [0]*N
    for _ in range(M):
        a,b = map(int, input().split())
        A[a-1] += 1
        A[b-1] += 1
    for a in A:
        if a%2 == 1:
            print("NO")
            return
    print("YES")

if __name__ == '__main__':
    main()
