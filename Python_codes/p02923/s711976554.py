N = int(input())
H = list(map(int, input().split()))
Ans = 0
c = 0
h = H[0]
for i in H[1:]:
    if h - i >= 0:
        c += 1
    else:
        if c > Ans :
            Ans = c
        c = 0
    h = i
if c > Ans :
    Ans = c
print(Ans)