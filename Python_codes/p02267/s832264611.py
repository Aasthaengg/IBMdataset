# coding: utf-8
# linearSearch
def linear(n,s,key):
    s[n:] = [key]
    i = 0
    while s[i] != key:
        i += 1
    return i != n
n = int(input())
s = list(map(int,input().split()))
input()
t = list(map(int,input().split()))
cnt = 0
for i in t:
    if linear(n,s,i):
        cnt += 1
print(cnt)