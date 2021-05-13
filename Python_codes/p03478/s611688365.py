# 083 B
N,A,B = map(int, input().split())
t = 0
for i in range(N):
    s =0
    n = i+1
    while n > 0:
        s += n%10
        n = int(n/10)
    if (s >= A)and(s <= B):
        t += (i+1)
print(t)