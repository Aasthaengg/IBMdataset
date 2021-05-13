A,B=map(int,input().split())
print(min(A,B)+abs(A-B)//2 if abs(A-B)//2*2==abs(A-B) else 'IMPOSSIBLE')