x=int(input())
count=0
for i in range(1,x**2+3):
    count+=i
    if count>=x:
        break
print(i)
