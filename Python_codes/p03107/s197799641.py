s = input()

zero = 0
one = 0

for c in s:
    if c == '1':
        one +=1
    else :
        zero +=1

print(min(one,zero)*2)