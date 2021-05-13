n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
ab = 21
m = 0
for i in a:
    m += b[i-1]
    if i == ab + 1:
        m += c[i-2]
    ab = i
print(m)