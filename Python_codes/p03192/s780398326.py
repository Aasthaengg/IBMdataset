N=input()

seek=0

for i in range(4):
    a=int(N[i:i+1])
    if a==2:
        seek+=1

print(seek)