s=input()
for _ in[0]*int(input()):
 a=input().split()
 o=a[0];i,j=map(int,a[1:3]);j+=1
 if'p'==o[0]:print(s[i:j])
 else:s=s[:i]+(a[3]if'p'==o[2]else s[i:j][::-1])+s[j:]
