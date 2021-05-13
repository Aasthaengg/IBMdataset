def popcount(x):
    return bin(x).count("1")

def f(x):
    if x == 0:
        return 1
    return f(x%popcount(x))+1

n = int(input())
x = input()
xx = int(x,2)
p = x.count("1")
stand1 = xx%(p+1)
if p != 1:
    stand2 = xx%(p-1)
for i in range(n):
    if x[i] == "1":
        if p != 1:
            k = stand2
            k -= pow(2,n-i-1,p-1) 
            k %= p-1
        else:
            print(0)
            continue
    else:
        k = stand1
        k += pow(2,n-i-1,p+1)
        k %= p+1
    print(f(k))