n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

point = 0
before = 10**10

for i in range(n):
    point += b[a[i]-1]
    if a[i] == before+1:
        point += c[a[i-1]-1]
    before = a[i]

print(point)