N = int(input())
a = list(map(int,input().split()))

num=0
rate=[0]*9
for i in range(N):
    dam=a[i]
    if dam<400:
        rate[0] = 1
    elif dam<800:
        rate[1] = 1
    elif dam<1200:
        rate[2] = 1
    elif dam<1600:
        rate[3] = 1
    elif dam<2000:
        rate[4] = 1
    elif dam<2400:
        rate[5] = 1
    elif dam<2800:
        rate[6] = 1
    elif dam<3200:
        rate[7] = 1
    else:
        rate[8] += 1

color = sum(rate[0:8])
# print(rate, val)

dai = color + rate[8]

if rate[8]==0:
    syo=color
else:
    if color==0:
        syo=1

    else:
        syo=color

print(syo,dai)
