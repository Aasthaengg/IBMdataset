N = int(input())
A = list(map(int, input().split()))

x = [0]*8
god = 0
for a in A:
    for i in range(8):
        if a < 400*(i+1):
            x[i] = 1
            break
    else:
        god += 1

res = sum(x)
print(max(res, 1), res+god)