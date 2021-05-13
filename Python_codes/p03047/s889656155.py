# coding: utf-8
# Your code here!
num = input().split()
num1 = int(num[0])
retu = int(num[1])
kazu = 0
hint=[]
for i in range(num1):
    hint.append(i)
while len(hint) >= retu:
    kazu+=1
    hint.pop(0)
print(kazu)
