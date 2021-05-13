j=input();i=52;a=[""]*i
while i:i-=1;a[i]="SHCD"[i/13]+" "+str(i%13+1)
while j:j-=1;a.remove(raw_input())
for i in a:print i