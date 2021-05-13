a,b,x = map(int, input().split())

count=0
if a==0 :
    count+=1

if a<=x :
    ai = x
else:
    ai = (a//x)*x
    if ai<a :
        ai +=x
if ai<=b :
    count+=1
    count+=(b-ai)//x

print(count)
