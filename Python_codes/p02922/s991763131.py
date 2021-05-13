A,B=map(int,input().split())
count=0
tap=1
while B>tap:
    count+=1
    tap+=A-1
print(count)