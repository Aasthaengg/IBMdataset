N,A,B = map(int,input().split())

sub = B-A-1
ans = ''
if sub%2==0:
    ans = 'Borys'
else:
    ans = 'Alice'
    
print(ans)
