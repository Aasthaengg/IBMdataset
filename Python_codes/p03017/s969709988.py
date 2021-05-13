import re
n,a,b,c,d = map(int,input().split())
s = input()
a,b,c,d = map(lambda x:x-1,[a,b,c,d])

#<##>が存在すると飛べないのでNG
#c>dの場合には、途中でaがbを追い抜く必要がある。そのスペース=<...>が
#あるか判定
if re.search(r'##',s[a:max(b,d)+1]):
    print('No')
else:
    if c>d:
        if (re.search(r'\.{3,}',s[b-1:d+2])):
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')