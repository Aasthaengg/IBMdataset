s=input()
K=int(input())
e=set()
for i in range(len(s)):
    for j in range(1,6):
        if(i+j>len(s)):
            break
        e.add(s[i:i+j])
li=sorted(e)
print(li[K-1])