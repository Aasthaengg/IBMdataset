def resolve():
    N = int(input())
    S = input()
    am = [0]
    ans = 0
    for i in range(N):
        if S[i] == "I":
            ans += 1
        if S[i] == "D":
            ans -= 1
        am.append(ans)
    print(max(am))
resolve()