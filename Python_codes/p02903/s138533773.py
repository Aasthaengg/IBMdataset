H,W,A,B = map(int,input().split())
ans = []
for i in range(B):
    a = min(A,W-A)
    ans.append('0'*a + '1'*(W-a))
for i in range(H-B):
    a = min(A,W-A)
    ans.append('1'*a + '0'*(W-a))
print(*ans, sep='\n')