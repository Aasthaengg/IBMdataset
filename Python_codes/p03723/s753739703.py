a,b,c = map(int,(input().split()))
cnt = 0

while a%2==0 and b%2==0 and c%2==0:
    if a == b == c :
        cnt = -1
        break
    ta,tb,tc = a,b,c
    a = tb/2 + tc/2
    b = ta/2 + tc/2
    c = ta/2 + tb/2
    cnt += 1

print(cnt)
