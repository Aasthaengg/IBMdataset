import math
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

def roundup(n):
    return int(math.ceil(n /10)) * 10
def get_digit(number):
    return number % 10   
s = 0
m = []
li = [A, B, C, D, E]
for i in range(len(li)):
    if get_digit(li[i]) >= 1:
        m.append(get_digit(li[i]))
f = False
m.sort()        
for l in range(len(li)):
    if len(m) > 0:
        if m[0] == get_digit(li[l]) and f == False:
            s += li[l]
            f = True
        else:
            s += roundup(li[l])
            # print(roundup(li[l]))
    else:
        s =sum(li)
print(s)