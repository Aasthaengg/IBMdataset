X, Y = input().split()

ans = "="

if X < Y:
    ans = "<"
elif X > Y:
    ans = ">"
    
print(ans)