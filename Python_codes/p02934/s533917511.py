a = int(input())
b = list(map(int,input().split()[:a]))
c = 0
for i in range(0, len(b)):
    d = 1/b[i] 
    c += d
e = 1/c
print(e)