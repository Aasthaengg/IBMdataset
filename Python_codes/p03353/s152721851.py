s = input()
K = int(input())
 
l = len(s)
 
sub = []
 
for i in range(l):
    for j in range(K):
        sub.append(s[i:min(i+j+1,l)])

#print(sub)
subl = list(set(sub))

subl.sort()
#print(subl)
 
print(subl[K-1])