import sys
input = sys.stdin.readline

#n = int(input())
#l = list(map(int, input().split()))

'''
A=[]
B=[]
for i in range():
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)'''
cnt=0
s=list(input())
t = list(input())
if s[0]==t[0]: cnt+=1
if s[1]==t[1]: cnt+=1
if s[2]==t[2]: cnt+=1
print(cnt)