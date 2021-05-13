def solve():
    n = int(input())
    keta = [0] * (n+1)
    for i in range(2, n+1):
        for j in range(2, int(pow(i, 0.5))+1):
            if i % j: continue
            ex = 0
            while i % j == 0:
                i = i // j
                ex += 1
            keta[j] += ex
        if i != 1:
            keta[i] += 1

    mod = 1000000007
    ans = 1
    for ex in keta:
        ans = ans * (ex + 1)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    solve()