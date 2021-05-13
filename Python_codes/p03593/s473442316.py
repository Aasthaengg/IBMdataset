
H,W = map(int,input().split())

dic = {}

for i in range(H):

    s =  input()

    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

n4 = 0
n2 = 0
n1 = 0

for i in dic:

    n4 += dic[i] // 4
    dic[i] = dic[i] % 4
    n2 += dic[i] // 2
    dic[i] = dic[i] % 2
    n1 += dic[i]


if H % 2 == 0 and W % 2 == 0:

    if n2 == 0 and n1 == 0:
        print ("Yes")
    else:
        print ("No")

elif H % 2 == 0 and W % 2 == 1:

    if n1 == 0 and n2 <= H // 2:
        print ("Yes")
    else:
        print ("No")

elif H % 2 == 1 and W % 2 == 0:

    if n1 == 0 and n2 <= W // 2:
        print ("Yes")
    else:
        print ("No")

else:

    if n1 <= 1 and n2 <= H // 2 + W // 2:
        print ("Yes")
    else:
        print ("No")
