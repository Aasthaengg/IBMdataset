X = int(input())

for i in range(1,361):
    if (360*i)%X==0:
        ans=(360*i)//X
        break
print(ans)
