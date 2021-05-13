from collections import Counter
S = input()
nums = list(set(S))
ans=pow(10,9)
for num in nums:
    s=S
    ans2=0
    while len(Counter(s)) > 1:
        list_s=list(s)
        new_s=[]
        for n in range(len(list_s)-1):
            if list_s[n] == num or list_s[n+1] == num:
                new_s.append(num)
            else:
                new_s.append(list_s[n])
        s = new_s
        ans2 += 1
    ans =  min(ans, ans2)
print(ans)
