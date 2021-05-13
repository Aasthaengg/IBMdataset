n=int(input())
for i in range(100,1000):
    if i >= n and i%100//10 == i%10 == i//100:
        print(i)
        break