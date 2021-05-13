n = int(input())
x = sorted(map(int,input().split()))
x.reverse()
a = 0
b = 0
for i in range(n):
    if i%2==0:
        a+=x[i]
    else:
        b+=x[i]
print(a-b)