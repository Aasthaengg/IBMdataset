n = int(input())

div = 1000000000+7

p10 = pow(10,n)
p9 = pow(9,n)
p8 = pow(8,n)


ans = p10-2*p9+p8
ans %= div

print(ans)
