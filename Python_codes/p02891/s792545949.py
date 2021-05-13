s = input()
k = int(input())

vals = []
cur = s[0]
strk = 1

for i in range(1, len(s)):
    if s[i] == cur:
        strk += 1
    else:
        vals.append([cur, strk])
        cur = s[i]
        strk = 1
vals.append([cur, strk])

if len(vals) == 1:
    print((vals[0][1] * k) // 2)
else:
    if vals[0][0] == vals[-1][0]:
        start = vals[0][1] // 2
        join = (vals[0][1] + vals[-1][1]) // 2
        end = vals[-1][1] // 2

        middle = 0
        for i in range(1, len(vals)-1):
            middle += vals[i][1] // 2

        print(start + k*middle + (k-1)*join + end)
    else:
        cnt = 0
        for val in vals:
            cnt += (val[1]) // 2

        print(cnt*k)