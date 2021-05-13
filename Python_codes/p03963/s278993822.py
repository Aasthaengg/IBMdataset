balls, colors = map(int, input().split())

ans = 1
for i in range(balls):
    if i == 0 :
        ans *= colors
    else:
         ans *= colors - 1
         
print(ans)