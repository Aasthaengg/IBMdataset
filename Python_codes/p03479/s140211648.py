X, Y = map(int, input().split())

a=X
cnt=1
while a <= Y:
    a *= 2
    if a <= Y:
        cnt+=1
print(cnt)