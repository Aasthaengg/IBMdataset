def mi():
    return map(int, input().split())

def main():
    S = input()
    N = len(S)+1
    l = [0]*N
    r = [0]*N
    ans = 0

    for i in range(N-1):
        if S[i] == '<':
            l[i+1] = l[i]+1
    for i in range(N-2, -1, -1):
        if S[i] == '>':
            r[i] = r[i+1]+1

    for i in range(N):
        ans += max(l[i], r[i])

    print(ans)

if __name__ == '__main__':
    main()
