
def solve():
    t = [0] * (N+1)
    for i in range(N):
        if S[i:i+2] == "AC":
            t[i+1] = t[i] + 1
        else:
            t[i+1] = t[i]
    for j in range(Q):
        print(t[lr[j][1]-1]-t[lr[j][0]-1])

if __name__ == "__main__":
    N,Q = list(map(int, input().split()))  
    S = input()
    lr = [list(map(int, input().split())) for _ in range(Q)]
    solve()
