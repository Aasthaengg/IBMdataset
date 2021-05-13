X= int(input())
A = int(input())
B = int(input())

X -= A
ans = X - ((X//B) * B)
print(ans)