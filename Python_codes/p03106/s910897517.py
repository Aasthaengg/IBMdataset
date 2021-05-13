a,b,k = map(int,input().split())
t = []
for i in range(1,100+1):
    if a % i == 0 and b % i == 0:
        t.append(i)
t.sort(reverse=True)
print(t[k-1])