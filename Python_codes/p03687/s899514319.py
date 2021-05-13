s = input()
ans = 10**18

for i in range(26):
    #print(chr(i+65+32))
    cnt = 0
    tmp = 0
    if s.count(chr(i+65+32)) == 0:
        continue
    #print(chr(i+65+32))
    for j in range(len(s)):
        if s[j] == chr(i+65+32):
            tmp = max(tmp,cnt)
            cnt = 0
        else:
            cnt += 1
    tmp = max(tmp,cnt)
    #print(tmp,cnt,ans)
    ans = min(ans,tmp)
            
print(ans)