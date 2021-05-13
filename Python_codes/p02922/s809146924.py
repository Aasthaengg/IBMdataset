a,b = map(int,input().split())
som = 1
cnt = 0
f = 0
while(som < b):
    som = som+a-1
    cnt = cnt+1
    if som >= b:
        f = 1
        break

print(cnt)