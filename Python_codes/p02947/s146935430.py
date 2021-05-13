n = int(input())
s = []
for i in range(n):
    s.append(input())
    
dic = dict()
ans = 0
for i in s:
    if "".join(sorted(i)) in dic:
        ans += dic["".join(sorted(i))]
        dic["".join(sorted(i))] +=1
    else:
        dic["".join(sorted(i))] = 1
print(ans)