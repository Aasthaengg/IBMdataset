[N,X] = list(map(int,input().split()))
m = []
for i in range(N):
    m.append(int(input()))
# print('m:',m)
amari = X - sum(m)
# print('amari:',amari)

i=0
while True:
    if amari<min(m)*i:
        ans = len(m) + i-1
        break
    i+=1
print(ans)
