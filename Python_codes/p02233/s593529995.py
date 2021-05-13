x = [1,1]
n = int(input())
for i in range(n):
    a=[x[i]+x[i+1]]
    x = x+a
print(x[n])
