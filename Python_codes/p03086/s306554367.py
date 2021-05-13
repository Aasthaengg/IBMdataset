s = str(input())
'''
ans = 0
memo = 0

for i in range(len(s)):
    if s[i] != "A" and s[i] !="C" and s[i] != "G" and s[i] !="T":
        if i-memo > ans:
            ans = i-memo
        memo = i+1
        #print(memo, ans, i)

print(ans)



'''
ans = 0
memo = 0

for i in range(len(s)):
    if s[i] == "A" or s[i] =="C" or s[i] == "G" or s[i] =="T":
        memo += 1
    else:
        if ans < memo:
            ans = memo
            memo = 0
if ans < memo:
    ans = memo


print(ans)