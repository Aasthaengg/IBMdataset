A, B, C = map(int,input().split())
K = int(input())

#赤＜緑＜青
kB = 0
kC = 0

while A >= B:
    B *= 2
    kB += 1

while B >= C:
    C *= 2
    kC += 1

if kB + kC <= K:
    print("Yes")
else:
    print("No")