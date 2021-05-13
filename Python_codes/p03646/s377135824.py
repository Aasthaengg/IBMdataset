import sys
input = sys.stdin.readline
INF = 10**20
MOD = 10**9 + 7

def main():
    k = int(input())
    print(50)

    l = (k + 49) // 50
    mod = k % 50
    ans = [l] * 50

    for i in range(50):
        ans[i] += 50 - i - 1
    
    if mod != 0:
        for i in range(50 - mod):
            for j in range(50):
                if i == j:
                    ans[j] -= 50
                else:
                    ans[j] += 1
    print(*ans)

if __name__=='__main__':
    main()