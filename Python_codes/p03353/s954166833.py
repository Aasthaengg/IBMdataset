s=str(input())
k=int(input())

l=len(s)
chars=set()
chars1=set()
sub1=['']*l

for j in range(l):
    chars1.add(s[j])
    min_c=sorted(chars1)[0]

def subset(st,m):
    substring=set()
    if m==0:
        lst=len(st)
    else:
        lst=m
    for i in range(lst):
        n=i+1 #length = n
        for j in range(lst-i):
            substring.add(st[j:j+n])
    return substring
    
chars=chars|subset(s[max(l-10,0):],0)
for i in range(l):
    if s[i]==min_c:
        chars=chars|subset(s[i:i+5],0)

#print(min_c,chars)

'''
for i in range(l):
    n=i+1 #length = n
    for j in range(l-i):
        chars.add(s[j:j+n])
        #print('i,j,sub',i,j,s[j:j+n])
'''

print(sorted(chars)[k-1])
