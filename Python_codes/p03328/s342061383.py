a,b = map(int,(input().split()))

def s(N):
    c = 0
    for i in range(1,N+1):
        c += i
    return c

print(s(b-a)-b)