N = int(input())
A= N//1000
B = (N - A*1000) //100
C = (N - A*1000 - B*100) // 10
D = N - A*1000 - B*100 - C*10
if A == B == C:
 print("Yes")
elif B==C==D:
 print("Yes")
else:
 print("No")