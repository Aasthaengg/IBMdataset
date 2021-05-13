N = int(input())
T = 0
A = 0
for _ in range(N):
    t, a = map(int, input().split())
    i = max(T//t, A//a, 1)
    while T > i*t or A > i*a:
        i += 1
    T = i*t
    A = i*a
    
print(T+A)