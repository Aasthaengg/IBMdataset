N,A,B=map(int, input().split())

C = A+B
q=N//C
r=N%C

ans = q*A
ans += A if r >= A else r
print(ans)