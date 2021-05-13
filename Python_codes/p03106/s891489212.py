a,b,k = map(int, input().split())
s = []
for i in range(1,101):
    if a % i == 0 and b % i == 0:
        s.append(i)
    if i > a or i > b:
        break
print(s[-k])
