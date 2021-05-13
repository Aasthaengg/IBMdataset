A,B,C = map(int,input().split())
m = max(A,B,C)*3
s = A+B+C
ans = m-s
if ans%2 == 1:
    ans += 3
print(ans//2)