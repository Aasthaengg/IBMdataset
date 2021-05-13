x=int(input())
s=100
count=0
while x>s:
    s+=s//100
    count+=1
print(count)