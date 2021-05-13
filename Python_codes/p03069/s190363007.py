n = int(input())
s = input()

black = []
white = []

cb=0
cw=0
for l in s:
    if l =="#":
        cb+=1
    else:
        cw+=1
    black.append(cb)
    white.append(cw)

if n == 1:
    print(0)
else:
    ans = [white[-1],black[-1]]
    for i in range(n):
        ans.append(black[i-1]+white[-1]-white[i-1])
    print(min(ans))



