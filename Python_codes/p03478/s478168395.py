N,A,B = map(int, input().split())
an = 0
for i in range(1,N+1):
    a = i
    t = 0
    while a > 0:
        t += a % 10
        a = a //10
    if t >= A and t <= B:
        an += i
print(an)