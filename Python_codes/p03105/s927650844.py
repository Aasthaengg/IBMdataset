a, b, c = map(int, input().split())

kikeru = b//a

if kikeru >= c:
    ans = c
else:
    ans = kikeru
    
print(ans)