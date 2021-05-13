s=input()
t=input()
cnt=0
mod=-1
tmp_s=""
for cha in t:
    if cha not in s:
        print(-1)
        exit()
    elif cha in tmp_s:
        idx=tmp_s.find(cha)
        mod+=idx+1   
    else:
        idx=s.find(cha)
        if idx<=mod:
            cnt+=1  
        mod=idx
    
    if mod==len(s)-1:
        tmp_s=" "
    else:
        tmp_s=s[mod+1:]

print(len(s)*cnt+mod+1)