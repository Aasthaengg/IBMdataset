n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

if sum(A)<sum(B):
    print(-1);exit()
s_ab = sorted(list(i-j for i,j in zip(A,B)))
s = 0
c = 0
for i in s_ab:
    if i<0:
        s+=i
        c+=1
    else:
        break
s_ab = s_ab[::-1]
for i in s_ab:
    if s<0:
        s+=i
        c+=1
    else:
        break
print(c)