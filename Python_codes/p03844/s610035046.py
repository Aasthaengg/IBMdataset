A,op,B = [str(i) for i in input().split()]

if op == '+':
    ans = int(A)+int(B)
else:
    ans =int(A)-int(B)
    
print(ans)