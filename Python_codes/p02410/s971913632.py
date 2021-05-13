n,m = map(int,raw_input().split())
a = [map(int,raw_input().split()) for _ in range(n)]
b = [input() for _ in range(m)]
for vec in a:
    sum=0
    for i in range(len(vec)):
        sum = sum + (vec[i] * b[i])
    print sum