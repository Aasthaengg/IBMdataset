a,b = map(int,input().split())
s = 1
cnt = 0
while (s < b):
    s = (s-1) + a 
    cnt += 1
print(cnt)