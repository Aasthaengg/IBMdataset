n,m=map(int,input().split())
drink=[list(map(int,input().split())) for i in range(n)]
#print(drink)

drink.sort()
#print(drink)
money=0
number=0
for i in range(n):
    if number+drink[i][1]<=m:
        money+=drink[i][0]*drink[i][1]
        number+=drink[i][1]
    elif m<number+drink[i][1]:
        money+=drink[i][0]*(m-number)
        number+=m-number
        break
    if m==number:
        break
print(money)