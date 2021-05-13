alf=[chr(ord('a') + i) for i in range(26)]

s=input()

for i in s:
    if i in alf:
        alf.remove(i)

if len(alf) > 0:
    print(s+alf[0])
else:
    if s=='zyxwvutsrqponmlkjihgfedcba':
        print(-1)
        exit()
    else:
        ans=[]
        for i in range(1,27):
            for j in ans:
                if s[-i]<j:
                    print(s[:26-i]+j)
                    exit()
            ans.append(s[-i])
            ans.sort()