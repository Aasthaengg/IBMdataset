n = int(input())
a = list(map(int, input().split()))
b = []; c = 0
while len(a) > 0:
    for j in range(len(a)):
        if a[-j-1] == len(a)-j: b.append(a.pop(-j-1)); break
    else: c = 1; break
else:
    b.reverse()
    for i in range(n):
        if b[i] > i+1: c = 1
print(-1) if c == 1 else print(*b, sep="\n")