a,v = list(map(int,input().split()))
b,w = list(map(int,input().split()))
t = int(input())

if w >= v:
    print('NO')
elif abs(a-b)/(v-w) <= t:
    print('YES')
else:
    print('NO')
