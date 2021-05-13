a,b = map(int,input().split())
dic1 = [0 for _ in range(10**3+1)]
dic2 = [0 for _ in range(10**3+1)]

for i in range(1,10**3+1):
    tax = i * 0.08
    tax2 = i * 0.1
    dic1[i] = int(tax)
    dic2[i] = int(tax2)

for i in range(10**3+1):
    if dic1[i] == a and dic2[i] == b:
        print(i)
        exit()
print(-1)