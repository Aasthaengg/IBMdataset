n = int(input())
s = [int(input()) for _ in [0]*n]
sm = sum(s)
if sm%10:
    print(sm)
else:
    s.sort()
    for i in range(n):
        if s[i]%10:
            print(sm-s[i])
            break
    else:
        print(0)