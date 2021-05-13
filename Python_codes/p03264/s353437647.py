k=int(input())
odd_count=0
for i in range(1,k+1):
    if i%2!=0:
        odd_count+=1

print(odd_count*(k-odd_count))
