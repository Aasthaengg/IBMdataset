x = [0]*5
for i in range(3):
    a,b = map(int, input().split())
    x[a]+=1
    x[b]+=1
print('NO'if 3 in x else'YES')