# coding: UTF-8
def euclidean_algorithm(x,y):
    if x > y:
        p = y
        r = x%y
        while r != 0:
            a = p
            b = r
            p = b
            r = a%b
        return p
    elif x == y:
        return x
    elif x < y:
        p = x
        r = y%x
        while r != 0:
            a = p
            b = r
            p = b
            r = a%b
        return p

num1,num2 = raw_input().split()
maximam = euclidean_algorithm(int(num1), int(num2))
print(maximam)

