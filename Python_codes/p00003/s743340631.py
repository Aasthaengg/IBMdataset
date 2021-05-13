while True:
    n = int(input())
    if n <= 1000:
        break

for i in range(1, n+1):
    l = list(map(int, input().split()))
    l.sort()
    if l[0]*l[0]+l[1]*l[1] == l[2]*l[2]:     
        print('YES')
    else :
        print('NO')
