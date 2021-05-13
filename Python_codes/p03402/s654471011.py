a, b = map(int, input().split())
Ans = [ ['.']*100 for _ in range(50) ]+[ ['#']*100 for _ in range(50) ]
for i in range(b-1):
    x, y = (i%50)*2, (i//50)*2
    Ans[y][x] = "#"
for i in range(a-1):
    x, y = (i%50)*2, 51+(i//50)*2
    Ans[y][x] = "."
print(100, 100)
for ans in Ans:
    print(''.join(ans))