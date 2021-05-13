a,b=map(int, input().split())

A = int(a/0.08)
B = int((b+1)/0.1)
l =['-1']

for i in range(A,B+1):
    if int(i*0.08) == a and int(i*0.1) == b:
        l.append(i)
        break
        
print(l[-1])