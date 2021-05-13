s = input()
ans = 0
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        t = s[i:j]
        if (all(map(lambda x:x in ['A','C','G','T'],t))):
            ans = max(len(t),ans)
print(ans)

        


