R, G, B, N = map(int, input().split())

def it():
    for i in range(N//R+1):
        r = R*i
        for j in range((N-r)//G+1):
            g = G*j
            b = N - r - g
            if b % B == 0:
                yield 1

print(sum(it()))
