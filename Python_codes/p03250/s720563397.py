num = list(map(int,input().split()))
num = sorted(num,reverse=True)

print(num[0]*10+num[1]+num[2])
