N,A,B = map(int,input().split())

h = []

for i in range(N):
    h.append(int(input()))

def det(num):
    count = 0
    for i in range(N):
        H = h[i]-B*num
        count += max(0,H//(A-B) + min(1,H%(A-B)))
    if count <= num:
        return True
    else:
        return False

x = 1###False
y = max(h)###True

while y - x > 1:
    if det((x+y)//2):
        y = (x+y)//2
    else:
        x = (x+y)//2
    #print(x,y)

print(y)