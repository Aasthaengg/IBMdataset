s = input()
n = len(s)
count = 0
sikii = [0]*(n+1)
for i in range(n-1):
    if s[i] != s[i+1]:
        sikii[i+1] = 1
#print(sikii)
print(sum(sikii))