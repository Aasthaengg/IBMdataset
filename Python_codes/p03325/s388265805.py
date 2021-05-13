
def solve():
    cnt = 0
    for i in range(N):
        tmp = 0
        while a[i]%2 == 0:
            a[i] /= 2
            tmp += 1  
        cnt += tmp
    print(cnt)

if __name__ == "__main__":
    N = int(input())
    a = list(map(int, input().split()))
    solve()
