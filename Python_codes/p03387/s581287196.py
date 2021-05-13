X = list(map(int, input().split()))
Y = sorted(X)
ans = 0
if Y[0]%2==Y[1]%2 and Y[1]%2 != Y[2]%2:
  ans +=1
  Y = [Y[0]+1,Y[1]+1,Y[2]]
elif Y[1]%2==Y[2]%2 and Y[2]%2 != Y[0]%2:
  ans +=1
  Y = [Y[0], Y[1]+1,Y[2]+1]
elif Y[2]%2==Y[0]%2 and Y[0]%2 != Y[1]%2:
  ans +=1
  Y = [Y[0]+1, Y[1], Y[2]+1]

A = Y[2]-Y[0]
B = Y[2]-Y[1]
C = min(A,B)
D = max(A,B)
ans += C + (D-C)//2
print(ans)