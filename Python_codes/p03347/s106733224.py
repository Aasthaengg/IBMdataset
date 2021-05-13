import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A.append(A[-1])
    
    if A[0] != 0:
        print(-1)
        exit()
    else:
        ans = 0
        now = 0
        for i in range(N):
            i += 1
            if A[i] == now + 1:
                now = A[i]
            elif A[i] == now:
                ans += now
            elif now > A[i]:
                ans += now
                now = A[i]
            else:
                print(-1)
                exit()
                
    print(ans)
    
if __name__ == "__main__":
    main()