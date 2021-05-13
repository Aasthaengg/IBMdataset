n, k, q = map(int, input().split())
a = list(int(input()) for i in range(q))
add = [0] * n
def func(x) :
    return k-q+x
for i in range(q) :
    add[a[i]-1] += 1
point = list(map(func, add))
for _ in range(n) :
    if point[_] <= 0 :
        print("No")
    else :
        print("Yes")
