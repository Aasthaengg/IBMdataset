n = int(input())
ans = 0
for i in range(n//7+1):
    if (n-i*7)%4 == 0:
        ans = 1
        break
print(["No","Yes"][ans])