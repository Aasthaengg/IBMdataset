A,B,C = list(map(int,input().split()))
count = 0
if A%2 == 1 or B%2 == 1 or C%2 == 1:
    print(0)
    exit()
if A == B == C:
    print(-1)
    exit()
while True:
    if A%2 == 1 or B%2 == 1 or C%2 == 1:
        break
    A_half = A//2
    B_half = B//2
    C_half = C//2
    A = B_half+C_half
    B = A_half+C_half
    C = A_half+B_half
    count += 1
print(count)