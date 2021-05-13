n = int(input())
a = list(map(int,input().split()))
a = [0] + a + [0]
a0 = a[0]
b = []
for i in range(1,n+2):
    b.append(abs(a0-a[i]))
    a0 = a[i]
s = sum(b)
for i in range(n):
    print(s+abs(a[i]-a[i+2])-(b[i]+b[i+1]))