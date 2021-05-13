# coding: utf-8
# Your code here!

D = int(input())
# with open("sample1.in") as f:

#c = [0 for i in range(26)]
s = [[0 for j in range(27)] for i in range(D)]
c = list(map(int, input().split(" ")))
result=[]
# for i in range(26):
#    c[i] = int(input())
for i in range(D):
    a = list(map(int, input().split(" ")))
    for j, k in enumerate(a):
        #print(i, j, k)
        s[i][j] = int(k)
    result.append(a.index(max(a))+1)
    #print(a.index(max(a)))

for i in range(D):
    # print(s.index(max(s[i])))
    print(result[i])

