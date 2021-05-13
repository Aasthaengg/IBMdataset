s = input().split()
a_have = int(s[0])
b_have = int(s[1])
for  i in range(int(s[2])):
    if i % 2 == 0:
        if a_have % 2 != 0:
            a_have-=1
        b_have+= a_have/2
        a_have = a_have/2
    else :
        if b_have % 2 != 0:
            b_have-=1
        a_have+= b_have/2
        b_have = b_have/2
print(int(a_have),int(b_have))
