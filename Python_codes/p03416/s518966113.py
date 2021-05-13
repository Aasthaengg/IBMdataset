A, B = map(int, input().split())

cnt=0
for x in range(A, B+1):
    l=[]
    while x>0 :
        r = x%10
        l.append(r)
        x //= 10
    if l[0]==l[4] and l[1]==l[3]:
        cnt +=1
print(cnt)