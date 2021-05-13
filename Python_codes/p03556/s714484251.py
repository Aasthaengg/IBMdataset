N=int(input())
maxi=0
for i in range(int(N**0.5)+1):
    if maxi<i**2:
        maxi=i**2
print(maxi)