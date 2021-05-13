n,c,k,*t=map(int,open(0).read().split())
t.sort()
busstart=t[0]
passenger=0
buscount=0
for i in t:
    if i>busstart+k or passenger==c:
        busstart=i
        passenger=1
        buscount+=1
    else:
        passenger+=1
print(buscount+1) 