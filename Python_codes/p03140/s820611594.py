N = int(input())
A = input()
B = input()
C = input()
ans = 0
for a,b,c in zip(A,B,C):
    if a==b==c: continue
    if a==b or b==c or c==a:
        ans += 1
    else:
        ans += 2
print(ans)