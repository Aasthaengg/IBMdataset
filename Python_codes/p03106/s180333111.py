a,b,k=map(int,input().split())
ls = []
for i in range(1,101):
    if a % i == 0 and b % i == 0:
        ls.append(i)
print(ls[-k])