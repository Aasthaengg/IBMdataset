n = int(input())
s = [input() for i in range(n)]

fi = 0
sec = 0
thi = 0
forth = 0

for i in range(n):
    cnt =  s[i].count("AB")
    if cnt>=1:
        fi+=cnt

    syo = s[i][0]
    saigo = s[i][-1]

    if syo =="B" and saigo == "A":
        sec+=1
    elif syo == "B":
        thi+=1
    elif saigo=="A":
        forth+=1

su=0
if sec>=1:
    su += sec-1

su+=fi

if sec>=1:
    su+=min(1,thi)
    su+=min(1,forth)
    su+=min(thi-min(1,thi),forth-min(1,forth))
else:
    su+=min(thi,forth)

#print(fi,sec,thi,forth)
print(su)
