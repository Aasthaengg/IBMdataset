f=lambda x:x[0]-2*x[1]+x[2]==0
print('YES' if f(list(map(int,input().split()))) else 'NO')