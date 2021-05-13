import string
low = string.ascii_lowercase
#print(low)
N = int(input())
st = ''
while N != 0:
    rem = N%26
    if rem == 0:
        rem = 26
    N -= rem
    N = N//26
    st += low[rem-1]
    #print(rem)
print(st[::-1])