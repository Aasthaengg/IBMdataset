from itertools import accumulate

def mi():
    return map(int, input().split())

def main():
    S = input()
    N = len(S)
    l = []
    r = []
    ans = [0]*N
    for i in range(N-1):
        if S[i:i+2] == 'LR':
            l.append(i)
        if S[i:i+2] == 'RL':
            r.append(i)

    l = [-1]+l+[N-1]

    for i in range(len(l)-1):
        for j in range(l[i]+1, l[i+1]+1):
            ans[r[i]+(j-r[i])%2] += 1

    print(' '.join(list(map(str, ans))))

if __name__ == '__main__':
    main()