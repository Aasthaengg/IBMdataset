n=int(input())
moti=[input() for i in range(n)]
moti.sort()
count=1
for i in range(n-1):
    if moti[i]!=moti[i+1]:
        count+=1
print(count)
