N = int(input())
a = N//100
if N >(a*111):
    b = a+1
    print(b*111)
else:
    print(a*111)