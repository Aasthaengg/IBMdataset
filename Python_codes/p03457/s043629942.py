N = int(input())
T = [0]
X = [0]
Y = [0]
for n in range(N):
  t,x,y = map(int,input().split())
  T.append(t)
  X.append(x)
  Y.append(y)

for n in range(N):
  D = abs(X[n+1]+Y[n+1]-X[n]-Y[n])
  if T[n+1]-T[n] == D:
    pass
  elif T[n+1]-T[n]>D and (T[n+1]-T[n]-D)%2==0:
    pass
  else:
    print("No")
    exit()
    
print("Yes")
