a,b,c = list(map(int,input().split()))
num = []
for i in range(a,b+1):
    if c % i == 0:
        num.append(i)
    else:
        continue
print(len(num))