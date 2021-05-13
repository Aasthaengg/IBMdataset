N = int(input())
for i in range(N,1000):
    x = str(i)
    if x[0]==x[1]==x[2]:
        break
print(x)