S=input()
count=0
string=""
queue=""
for s in S:
    queue+=s
    if string!=queue:
        count+=1
        string=queue
        queue=""
print(count)