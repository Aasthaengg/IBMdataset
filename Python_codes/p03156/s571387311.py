n = int(input())
a,b = map(int, input().split())
dat = list(map(int, input().split()))
q1=q2=q3=0
for i in range(n):
    if dat[i] <= a:
        q1 += 1
    elif a < dat[i] <= b:
        q2 += 1
    else:
        q3 += 1
print(min(q1,q2,q3))
