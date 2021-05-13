s = input()
#print(s[1])
#print(s[2])
i = list(range(0,len(s)+1,2))
temp =""
for t in range((len(s)+1)//2):
    temp = temp+s[i[t]]

print(temp)
