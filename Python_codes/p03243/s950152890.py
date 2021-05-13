n=list(input())

if int(n[0])>int(n[1]):
    ans = [n[0]]*3
elif int(n[0])==int(n[1]) and int(n[1])>=int(n[2]):
    ans = [n[0]]*3
else:
    ans = [int(n[0])+1]*3
print(*ans,sep="")