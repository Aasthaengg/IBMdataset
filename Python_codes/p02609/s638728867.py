def popcount(num):
    ans = 0
    while num:
        if num % 2 == 1:
            ans += 1
        num //= 2
    return ans


N = int(input())
X = input()

popcount_X = 0
for x in X:
    if x == "1":
        popcount_X += 1

tmp4p = int(X, 2) % (popcount_X+1)
if popcount_X != 1:
    tmp4m = int(X, 2) % (popcount_X-1)

for i in range(N):
    bit = X[i]

    f = 0
    if (popcount_X == 1 and bit == "1"):
        print(f)
        continue
    
    if bit == "1":
        nxt = ( tmp4m - pow(2, N-i-1, (popcount_X-1))  + (popcount_X-1) ) % (popcount_X-1)
    else:
        nxt = ( tmp4p + pow(2, N-i-1, (popcount_X+1))  ) % (popcount_X+1)

    f += 1
    while nxt:
        pc = popcount(nxt)
        nxt = nxt % pc
        f += 1
    
    print(f)
