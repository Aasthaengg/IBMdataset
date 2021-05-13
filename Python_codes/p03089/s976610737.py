
def resolve():
    N = int(input())
    B = list(map(int, input().split()))
    ans = []
    while B:
        for i in range(len(B) - 1, -1, -1):
            if B[i] == i + 1:
                ans.append(i + 1)
                del B[i]
                break
        else:
            print(-1)
            return 
    print(*ans[::-1], sep='\n')



if __name__ == "__main__":
    resolve()