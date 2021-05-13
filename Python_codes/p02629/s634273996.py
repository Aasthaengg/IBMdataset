N=int(input())
res=''
while N>0:
    N=N-1
    res +=chr(ord('a') + N%26)
    N=N//26
    
print(res[::-1])