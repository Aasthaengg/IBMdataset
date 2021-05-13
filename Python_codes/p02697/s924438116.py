N, M = map(int, input().split())
d = (N-1)//2
ans = [(1, 1+d)]

while True:
    a, b = ans[-1][0]+1, ans[-1][1]-1
    
    if a<b:
        ans.append((a, b))
    else:
        break

ans.append((2+d, 1+2*d))

while True:
    a, b = ans[-1][0]+1, ans[-1][1]-1
    
    if a<b:
        ans.append((a, b))
    else:
        break

for a, b in ans[:M]:
    print(a, b)