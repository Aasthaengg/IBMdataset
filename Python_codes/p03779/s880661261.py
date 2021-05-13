S=int(input())
t=0
for i in range(1,S+1):
    t+=i
    if t>=S:
        print(i)
        break