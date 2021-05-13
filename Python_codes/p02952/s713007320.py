# ABC136
# B Uneven Numbers
# N以下の整数で桁数が奇数のものの数
n = int(input())
ct = 0
for i in range(1,n+1):
    if len(str(i)) % 2:
        ct +=1
print(ct)
