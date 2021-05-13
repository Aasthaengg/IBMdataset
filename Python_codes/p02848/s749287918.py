# coding: utf-8
# Your code here!
n=int(input())

s=list(input())
for i in range(len(s)):
    if ord(s[i])+n>90:
        print(chr(ord(s[i])+n-26),end="")
    else:
        print(chr(ord(s[i])+n),end="")
    
