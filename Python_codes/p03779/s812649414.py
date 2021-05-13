x=int(input())
a=0
for i in range(10**5):
    a+=i
    if a>=x:
        print(i)
        break