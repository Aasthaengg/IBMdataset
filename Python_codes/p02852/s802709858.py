N, M = map(int, input().split())
S = input()
ANS = []

x = N
while x:
    for i in range(max(x-M, 0), x):
        if S[i] == "0":
            ANS.append(x-i)
            x = i
            break
    else:
        print(-1)
        break
else:
    print(*ANS[::-1])
