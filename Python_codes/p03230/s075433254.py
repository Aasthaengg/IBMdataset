import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    N = int(readline())

    K = 0
    for i in range(1,10**3):
        if i * (i-1) // 2 == N:
            K = i
            break

    if K == 0:
        print("No")
        exit()
    
    S = [[0] * (K-1) for _ in range(K-1)]

    a = 1
    for i in range(K-1):
        for j in range(i+1):
            S[i][j] = a
            S[j][i] = a
            a += 1

    ans = []
    for s in S:
        ans.append("{} {}".format(K-1, " ".join(map(str, s))))


    tri = [S[i][i] for i in range(K-1)]
    ans.append("{} {}".format(K-1, " ".join(map(str, tri))))

    print("Yes")
    print(K)

    print("\n".join(ans))

    
if __name__ == "__main__":
    main()
