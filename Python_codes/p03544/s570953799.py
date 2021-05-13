n=int(input())
num=[2,1]
for i in range(n-1):
    num.append(num[-1]+num[-2])
print(num[n])
