#n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
s=list(input())
flag='None'
alphabet=list('abcdefghijklmnopqrstuvwxyz')
dic={}
for si in s:
    dic[si]=True

for c in alphabet:
    if dic.get(c,False)==False:
        flag=c
        break
print(flag)