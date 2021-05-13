N, A, B = map(int, input().split())

df = abs(A - B)
dA = A - 1
dB = N - B
ans = 0

if df % 2 == 0:
    ans = int(df // 2)
    print(ans)
else:
    if dA > dB:
        #端までの距離
        ans += dB + 1 + ((B-A) // 2)
        print(ans)
    else:
        ans += dA + 1 + ((B-A) // 2)
        print(ans)

