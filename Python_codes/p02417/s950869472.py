sente=""
while True:
    try:
        t=input().lower()
        sente = sente+t
    except:
        break
for i in range(97,123):
    print(chr(i),":",sente.count(chr(i)))