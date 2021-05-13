a,b=map(int,input().split())

t=1
for i in range(21):
    t=1+(a-1)*i
    if t>=b:
        mini=i
        break
print(i)