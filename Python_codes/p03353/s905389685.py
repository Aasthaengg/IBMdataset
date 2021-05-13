s = input()
K = int(input())
subs = set()
for l in range(1,min(5,len(s))+1):
    for i in range(len(s)-l+1):
        subs.add(s[i:i+l])
subs = list(subs)
subs.sort()
print(subs[min(len(subs),K)-1])