s = int(input())

n = [0, 0, 1]

for i in range(3, s) :
    next_n = sum(n[0:i-2]) + 1
    n.append(next_n)

if s > 2 :
    print(n[-1] % (10**9 + 7))
else :
    print(0)