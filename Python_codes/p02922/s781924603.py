"""B - Power Socket """
A, B = map(int, input().split())

s=1
count=0
while(s<B):
    s=s-1+A
    count+=1


print(count)
