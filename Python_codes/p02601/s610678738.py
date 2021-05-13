A,B,C = map(int,input().split())
K = int(input())

ans = 0
while 1:
    if A < B:
        break
    else:
        B *= 2
        ans += 1

while 1:
    if B < C:
        break
    else:
         C *= 2
         ans += 1

if ans <= K:
    print("Yes")
else:
    print("No")