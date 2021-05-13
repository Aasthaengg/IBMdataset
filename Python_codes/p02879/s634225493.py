A,B = map(int, input().split())
if A // 10 > 0 or B // 10 > 0:
    print(-1)
else:
    print(A *  B)