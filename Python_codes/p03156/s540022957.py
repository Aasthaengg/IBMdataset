n = int(input())
A,B = map(int,input().split())
p = list(map(int,input().split()))
a1 = 0
for i in range(A+1):
    a1 += p.count(i)
a2 = 0
for i in range(A+1,B+1):
    a2 += p.count(i)
a3 = 0
for i in range(B+1,21):
    a3 += p.count(i)

print(min(a1,a2,a3))