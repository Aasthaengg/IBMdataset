x,k,d = map(int, input().strip().split(" "))

x = abs(x)
g = min(k, x//d)

x -= d*g
k -= g

if k%2 == 0:
    print(x)
else:
    print(abs(x-d))