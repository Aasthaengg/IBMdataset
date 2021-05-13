inp = list(map(int,input().split()))
a = inp[0]
b = inp[1]
c = inp[2]
n = 0
for i in range(a,b+1):
    if c%i == 0:
        n += 1
print(n)