A, B, C = sorted(map(int,input().split()))

if A == B and A == C:
    print(0)
    exit()
cnt = 0
cnt += (C - A) // 2
A = ((C - A) // 2) * 2 + A
cnt += (C - B) // 2
B = ((C - B) // 2) * 2 + B

if A == B and A == C:
    print(cnt)
elif A == B and A != C:
    print(cnt+1)
else:
    print(cnt+2)