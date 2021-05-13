
def solve():
    ans = "Yes"
    for i in range(1,N-1):
        if H[i] > H[i+1]:
            H[i] -= 1
            if H[i] > H[i+1]:
                ans = "No"
                break
            if H[i-1] > H[i]:
                ans = "No"
                break
        elif H[i-1] <= H[i]-1:
            H[i] -= 1
    print(ans)

if __name__ == "__main__":
    N = int(input())
    H = list(map(int, input().split()))  
    solve()
