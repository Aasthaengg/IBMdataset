N=int(input())

c=1
for i in range(1,50001):
    if int(i*1.08)==N:
        c=0
        print(i)
        
if c==1:
    print(":(")