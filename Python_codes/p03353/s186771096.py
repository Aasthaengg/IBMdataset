s = input()
k = int(input())
n = len(s)

substring = []

for i in range(min(n, k)):
    for j in range(n-i):
        substring.append(s[j:j+i+1])
        #print(s[j:j+i+1], j, j+i+1)

substring = list(set(substring))
substring.sort()
#print(substring)

print(substring[k-1])
