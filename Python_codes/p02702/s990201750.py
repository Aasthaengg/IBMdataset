def resolve():
    S = list(input())
    rem = [0 for _ in range(2019)]
    v = 0
    rem[0] += 1
    p = 1
    for i in range(len(S)-1, -1, -1):
        v = p*int(S[i]) + v
        v %= 2019
        rem[v] += 1
        p = (p*10)%2019

    ans = 0
    for r in rem:
        ans += r*(r-1)//2
    print(ans)
        



if '__main__' == __name__:
    resolve()