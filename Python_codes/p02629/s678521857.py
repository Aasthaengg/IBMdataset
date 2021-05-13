# coding: utf-8
# Your code here!
N=int(input())

ans=""

while N!=0:
    N-=1
    c=N%26
    N//=26
    ans+=chr(c+97)

print(ans[::-1])