line = input()
A, B, X = [int(u) for u in line.split()]
def func(a,b,x):
    return print("YES") if (x <a+b and x>=a) else print("NO")
func(A,B,X)