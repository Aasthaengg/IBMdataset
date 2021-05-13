A,B = map(int,input().split())
cnt = 0
for i in range(A,B+1):
    a = str(i)
    b = a[::-1]
    if a==b:
        cnt += 1
print(cnt)