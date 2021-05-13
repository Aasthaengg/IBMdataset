w= input().casefold()
 
cnt = 0
 
while(1):
    snt = input()
    if snt == "END_OF_TEXT":
        break
    sntt = snt.casefold()
    words = sntt.split()
    cnt += words.count(w)
     
print(cnt)