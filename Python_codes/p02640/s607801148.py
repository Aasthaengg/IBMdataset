# Crane and Turtle
X,Y=map(int,input().split())
def solve(X, Y):
    return (2*X - (1/2)*Y, -X + (1/2)*Y)
a, b = solve(X, Y)
ans = ['No', 'Yes'][((a>=0)&(b>=0))&((a%1==0)&(b%1==0))]
print(ans)
