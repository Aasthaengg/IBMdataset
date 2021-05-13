a,b=map(int, input().split())
c="必要な電源タップ数は"
d="個です。"
count=0
total=1
while True:
    
#    total+=a
    
#    if total<b:
#        total-=1
#        count+=1
#    else:
#        break
    if total >= b:
        break
    total += (a-1)
    count+=1
print(count)