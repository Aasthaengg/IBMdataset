A,B,C = map(int, input().split())
ans = 'NO'
for i in range(B):
    if ((A%B)*i)%B==C:
        ans = 'YES'
        break
        
print(ans)