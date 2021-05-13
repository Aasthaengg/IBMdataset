N = int(input())
cnt=0
y=[]

for i in range(1,N+1,2):
    for j in range(1,i+1):
        if i%j == 0:
            y.append(j)
    if len(y)==8:
        cnt += 1
    y.clear()
print(cnt)
