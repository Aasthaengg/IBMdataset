#B - Count Balls
N,A,B = map(int,input().split())

balls = N - (A+B)*(N//(A+B))#最後の一回の操作で加えることのできるボールの個数
if balls <= A:
    ans = A * (N//(A+B)) + balls
else:
    ans = A * (N//(A+B)) + A
print(ans)