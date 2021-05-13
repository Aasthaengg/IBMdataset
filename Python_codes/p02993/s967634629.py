s=list(input())
for i in range(0,len(s)-1):
    if s[i]==s[i+1]:
        print('Bad')
        break
else:
    print('Good')
