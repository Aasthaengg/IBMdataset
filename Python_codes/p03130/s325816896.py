s={1,2,3,4}
for i in range(3):
    s&=set(map(int,input().split()))
print('YES' if not s else 'NO')