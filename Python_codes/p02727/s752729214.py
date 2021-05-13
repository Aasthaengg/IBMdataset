X,Y,A,B,C = map(int,input().split())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
R = list(map(int,input().split()))

P.sort()
Q.sort()

all_apples = []
for i in range(max(X,Y,C)):
  if(i<X):
    all_apples.append([P[-(i+1)],'r'])
  if(i<Y):
    all_apples.append([Q[-(i+1)],'g'])
  if(i<C):
    all_apples.append([R[i],'any'])

all_apples.sort()

ans = 0
for i in range(X+Y):
 ans += all_apples[-(i+1)][0]
print(ans)