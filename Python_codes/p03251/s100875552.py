n, m, x, y = map(int, input().split())
l_X = list(map(int, input().split()))
l_y = list(map(int, input().split()))

l = []

for i in range(x+1, y+1):
    l.append(i)
    
for i in l:
    if max(l_X) < i:
        if min(l_y) >= i:
            print('No War')
            exit()
            
print('War')