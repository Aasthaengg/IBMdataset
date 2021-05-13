s = input()
k = int(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
n = len(s)
lis = set()
for i in range(26):
    for j in range(len(s)):
        if s[j] == alpha[i]:
            for l in range(j, j+k+1):
                if l < n:
                    lis.add(s[j:l+1])
lis = list(lis)
lis.sort()
#print(lis)
#print(k)
print(lis[k-1])