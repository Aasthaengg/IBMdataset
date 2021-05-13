a,b,c = map(int, input().split())

abc = [a,b,c]
abcs = sorted(abc)

ac =abcs[2]-abcs[0]
bc =abcs[2]-abcs[1]

res = 0

res += ac//2
res += bc//2

dx = ac % 2
dy = bc % 2

if dx + dy ==0:
    print(res)
elif dx + dy ==2:
    print(res+1)
else:
    print(res+2)