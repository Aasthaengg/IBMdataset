N = int(input())

for i in range(10**5):
    if i*(i+1)//2>=N:
        m = i
        break

a = m*(m+1)//2-N
ans = []

for i in range(1, m+1):
    if i==a:
        continue
    
    print(i)