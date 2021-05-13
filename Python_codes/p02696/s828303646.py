A,B,N = map(int,input().split())
if B-1 <= N:
    ans = A*(B-1)//B
else:
    ans = A*N//B
print(ans)
