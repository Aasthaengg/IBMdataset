n = int(input())
s = str(input())
if n%2==1:
    print('No')
else:
    m = int(n/2)
    #isError = False
    #for i in range(m):
    #    if s[i]!=s[i+m]:
    #        isError = True
    #        break
    #if isError:
    #    print('No')
    #else:
    #    print('Yes')
    #print(s[:m])
    #print(s[m:])
    if s[:m]!=s[m:]:
        print('No')
    else:
        print('Yes')
