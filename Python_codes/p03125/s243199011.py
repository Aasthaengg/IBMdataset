from sys import stdin
 
A,B = map(int,stdin.readline().strip().split())

ans = 0
if B%A==0:
    ans = A + B
else:
    ans = B - A

print(ans)    
