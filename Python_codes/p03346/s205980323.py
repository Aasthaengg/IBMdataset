import sys
input = sys.stdin.readline

def main():
    N = int(input())
    ind = [0 for _ in range(N)]
    for i in range(N):
        A = int(input())
        ind[A-1] = i

    ans = 0
    count = 0
    for i in range(N-1):
        if ind[i] < ind[i+1]:
            count += 1
        else:
            ans = max(ans,count)
            count = 0
        ans = max(ans,count)

    print(N-ans-1) 

if __name__ == "__main__":
    main()