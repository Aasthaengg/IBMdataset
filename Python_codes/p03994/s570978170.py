s = list(input())
k = int(input())
abc = "abcdefghijklmnopqrstuvwxyz"
c = 0
for e,i in enumerate(s):
    # print(26-abc.index(i))
    if k-26+abc.index(i)>=0 and i!='a':
        s[e] = 'a'
        k-=26-abc.index(i)
    # print(k)  
k+=abc.index(s[-1])
k%=26
s[-1] = abc[k]

print("".join(s))