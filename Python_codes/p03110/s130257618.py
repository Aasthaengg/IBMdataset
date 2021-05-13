N = int(input())
xu = []
for i in range(N):
    xu.append(list(input().split()))
#print(xu)

wa = 0
for i in range(N):
     if xu[i][1] == 'JPY':
         wa += int(xu[i][0])
     elif xu[i][1] == 'BTC':
         wa += float(xu[i][0]) * 380000
print(wa)