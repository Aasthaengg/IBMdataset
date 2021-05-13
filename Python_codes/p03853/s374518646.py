h,w = map(int, input().split())

c = []
for i in range(h):
    c.append(input())
    
for i in range(h):
    for j in range(2):
        print(c[i])