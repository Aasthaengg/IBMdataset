A,B,N = [int(x) for x in input().split()]

def f(x):
    return int(A*x/B) - A * int(x/B)

print(f(min(B-1,N)))