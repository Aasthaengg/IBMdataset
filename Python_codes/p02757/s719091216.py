N, P = map(int, input().split())
S = list(map(int, list(input())))

l = len(S)
if P == 2:
    ans = 0
    for i in range(l):
        if S[i]%2 == 0:
            ans += i+1
elif P == 5:
    ans = 0
    for i in range(l):
        if S[i]%5 == 0:
            ans += i+1
else:
    data = [0]*P
    temp = 0
    ans = 0
    for i in range(l-1, -1, -1):
        temp += S[i]*pow(10, l-i-1, P)
        temp %= P
        ans += data[temp]
        data[temp] += 1
    ans += data[0]

print(ans)