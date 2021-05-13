N = int(input())
L = [111*i for i in range(1,10)]
ans = 0
for l in L:
    if N <= l:
        ans = l
        break
print(l)