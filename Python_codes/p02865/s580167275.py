N=int(input())
num=N
count=0

while num>int(N/2):
    num-=1
    count+=1

print(count-1)        