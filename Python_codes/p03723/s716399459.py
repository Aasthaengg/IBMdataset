A,B,C = map(int, input().split())

ans = 0
for ans in range(1000):
    if A&1 or B&1 or C&1:
        print(ans)
        break
    A,B,C = (B+C)//2, (C+A)//2, (A+B)//2
else:
    print(-1)