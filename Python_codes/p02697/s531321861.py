N, M = map(int, input().split())
d = (N-1)//2
ans = []
ans.append((1, 1+d))

while True:
    a = ans[-1][0]+1
    b = ans[-1][1]-1
    
    if a>=b:
        break
    
    ans.append((a, b))

d2 = d-1
ans.append((2+d, 2+d+d2))

while True:
    a = ans[-1][0]+1
    b = ans[-1][1]-1
    
    if a>=b:
        break
    
    ans.append((a, b))

for a, b in ans[:M]:
    print(a, b)