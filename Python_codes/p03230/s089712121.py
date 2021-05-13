import sys
input = sys.stdin.readline

def main():
    N = int(input())
    g = 1
    tmp = 1
    while tmp < N:
        g += 1
        tmp += g
    if tmp != N:
        print("No")
        return
    ans = [list() for i in range(g+1)]
    i, j = 0, 0
    for count in range(N):
        if i == j:
            ans[i].append(count+1)
            ans[-1].append(count+1)
            i += 1
            j = 0
        else:
            ans[i].append(count+1)
            ans[j].append(count+1)
            j += 1
    print("Yes")
    print(g+1)
    for i in range(g+1):
        print(len(ans[i]), end=" ")
        for j in range(len(ans[i])-1):
            print(ans[i][j], end=" ")
        print(ans[i][-1])

if __name__ == "__main__":
    main()