x = int(input())

# 1,[2],3,[4,5],6,[7,8,9],10 ...

ans = (-1+(8*x+1)**0.5)/2
ans = -(-ans//1)

print(int(ans))