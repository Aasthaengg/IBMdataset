#coding: utf-8

S = input()
K = int(input())

# find not one
pos = None

for i in range(len(S)):
    if S[i] != "1":
        pos = i
        break

#print("pos=%d" % pos)

if pos == None:
    print("1")
else:
    if K <= pos:
        print("1")
    else:
        print(S[i])

