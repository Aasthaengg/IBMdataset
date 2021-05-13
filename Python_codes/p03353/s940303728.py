s = input()
K = int(input())

lst=[]
for length in range(1,K+1):
    for start in range(len(s)-length+1):
        lst.append(s[start:start+length])
#print(lst)
lst=sorted(list(set(lst)))
#print(lst)
print(lst[K-1])