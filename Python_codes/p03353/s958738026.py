s=input()
k=int(input())
l=len(s)
def find_substring_from_a(a):
    a_s=[]
    for i in range(l):
        if s[i]==a:
            for j in range(1,min(6,l-i+1 )):
                a_s.append(s[i:i+j])
    return sorted(set(a_s) )
moji_list = sorted(set(s))
length = 0
for a in moji_list:
    a_s=find_substring_from_a(a)
    lenas = len(a_s)
    if length+lenas >=k:
        break
    else:
        length+=lenas
print(a_s[k-length-1])