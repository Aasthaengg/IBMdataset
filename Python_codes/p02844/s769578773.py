n = int(input())
s = input()

cnt = 0
for i in range(1000):
    x = str(i).zfill(3)
    a = s.find(x[0])
    b = s[a+1:].find(x[1])
    c = s[a+b+2:].find(x[2])
    if -1 not in (a,b,c):
        cnt += 1
print(cnt)