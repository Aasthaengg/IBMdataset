n = input()

if len(list(n)) == 1:
    print(int(n))
    exit()

if set(list(n)) == {'9'}:
    print(len(list(n))*9)
    exit()

tmp = ''
for i in range(1,len(n)):
    if n[i] == '9':
        tmp += n[i-1]
    else:
        tmp += str(int(n[i-1])-1) + '9'*(len(n)-i)
        break
else:
    tmp += '9'

ans=0
for i in range(len(tmp)):
    ans += int(tmp[i]) 

print(ans)
