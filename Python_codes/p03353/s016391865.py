s = input()
k = int(input())
lst=[]
ls=len(s)
for i in range(ls):
    for j in range(i+1,min(ls+1,i+k+1)):
        lst.append(s[i:j])
lst=sorted(set(lst))
print(lst[k-1])