N = int(input())
A = N*(N+1)//2
P = N//3
B = 3*P*(P+1)//2
Q = N//5
C = 5*Q*(Q+1)//2
R = N//15
D = 15*R*(R+1)//2

ans = A - B - C + D
print(ans)
