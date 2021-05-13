s=input()
length=len(s)
now_length=length-2
ans=0
while True:
    if s[0:int(now_length/2)]==s[int(now_length/2):now_length]:
        ans=now_length
        break
    else:
        now_length=now_length-2
print(ans)