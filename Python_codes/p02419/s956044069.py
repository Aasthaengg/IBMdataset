W=input()
T=""
while True:
    tmp=input()
    if tmp=="END_OF_TEXT":
        break
    else:
        T+=tmp+" "

T=list(T.lower().split())
cnt=0
for word in T:
    if word==W:
        cnt+=1
print(cnt)
