import fractions


def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

def check():
    N, M = map(int, input().split())
    S = input()
    T = input()
    length = lcm(N,M)
        
    for i in [a*(length//N) for a in range(N)]:
        if i%(length//M)==0:
            if S[i//(length//N)] != T[i//(length//M)]:
                return -1
    return length
  
print(check())