import collections
s = input()
dic = collections.defaultdict(list)
for i in range(len(s)):
    dic[s[i]].append(i)
ans = 10000
for key in dic.keys():
    ls = [-1] + dic[key] + [len(s)]
    diff = []
    for i in range(len(ls)-1):
        diff.append(ls[i+1] - ls[i]-1)
    #print(diff)
    ans = min(max(diff),ans)
print(ans)
