s=input()
k=int(input())

sb=set()
for i in range(len(s)):
    for ii in range(i,i+k):
        if ii<len(s):
#            print(s[i:ii+1])            
            sb.add(s[i:ii+1])
sb2=list(sb)
sb2.sort()
print(sb2[k-1])
