N=int(input())
odd=0
for i in range(N+1):
    if i%2==0:
        continue
    else:
        odd+=1.0000
print(float(odd/N))