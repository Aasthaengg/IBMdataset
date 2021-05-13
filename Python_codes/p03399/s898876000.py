Bus=[]
Train=[]

for i in range(2):
    b=int(input())
    Bus.append(b)
for i in range(2):
    t=int(input())
    Train.append(t)
Bus.sort()
Train.sort()
print(Bus[0] + Train[0])