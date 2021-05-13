n = int(input())
s = list(map(str,input()))
ans = []
ans.append(0)
tmp = 0

for i in s:
    if i == "I":
        tmp += 1
        ans.append(tmp)
    else:
        tmp -= 1
        ans.append(tmp)
        
print(max(ans))