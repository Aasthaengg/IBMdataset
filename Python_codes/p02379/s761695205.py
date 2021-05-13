N = input().split()

z = ((float(N[0])-float(N[2]))**2)+((float(N[1])-float(N[3]))**2)
ans = z**0.5
print('{:.08f}'.format(ans))
