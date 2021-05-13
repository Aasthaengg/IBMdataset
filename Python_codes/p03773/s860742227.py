A,B = map(int, input().split())
Ans = A + B

if Ans <= 23:
    print(Ans)
else:
    print(Ans-24)