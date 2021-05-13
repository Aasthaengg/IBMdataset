n=int(input())
a=[int(x) for x in input().split()]
b=[y for y in a if y%2 == 0]
c=0
for i in b:
    if i%3 == 0 or i%5 == 0:
        pass
    else:
        print("DENIED")
        c=1
        break
        
if c==0:
    print("APPROVED")