N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
if sum(B) > sum(A):
  print("-1")
  exit()
D = []
for i in range(N):
  D.append(A[i]-B[i])
D.sort()
#print(D)
num = 0
s = 0; t = -1
yoyu = 0
while D[s] < 0:
  if yoyu+D[s] <0:
    num += 1 #ここで一番余裕があるのを取り出す。
    yoyu += D[t]
    t -= 1
  num += 1 #ここで足りない分が足された試験
  yoyu += D[s]
  s += 1
print(num)  