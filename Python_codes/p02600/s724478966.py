x=int(input())
now=400
for i in range(100):
    if now<=x<=now+199:
        print(8-i)
        break
    else:
        now+=200
