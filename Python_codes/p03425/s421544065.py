import itertools

n = int(input())

C = [0, 1, 2, 3, 4]

march = [0]*5
for i in range(n):
    a = input()
    if a[0] == "M":
        march[0] += 1
    elif a[0] == "A":
        march[1] += 1
    elif a[0] == "R":
        march[2] += 1
    elif a[0] == "C":
        march[3] += 1
    elif a[0] == "H":
        march[4] += 1
 
tst = list(itertools.combinations(C,3))

ans = 0
for i in range(10):
    ans += march[tst[i][0]] * march[tst[i][1]] * march[tst[i][2]]

print(ans)