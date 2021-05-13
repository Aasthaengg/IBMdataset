n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
x = 0
j = 25
for i in a:
    x += b[i-1]
    if i - j == 1:
        x += c[j-1]
    j = i
print(x)