#-------------
N = int(input())
T,A = map(int, input().split())
H =list(map(int, input().split()))
#-------------
Temp = []

for i in range(N) :
  Temp.append(T-0.006*H[i]-A)

Temp_abs=[]
for i in range(N) :
  Temp_abs.append(abs(Temp[i]))

cnt =1
for i in range(N):
  if min(Temp_abs) != Temp_abs[i]:
    cnt+=1
  else:
    print(cnt)