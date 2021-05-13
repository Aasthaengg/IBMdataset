# coding: utf-8
# Your code here!

N = int(input())
s = input()
t = input()

for i in range(N+1):
    string = s[:i]+t
    
    if string[:N] == s and string[-N:] == t:
        print(len(string))
        break