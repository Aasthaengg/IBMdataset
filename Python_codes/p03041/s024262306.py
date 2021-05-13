
n,k = map(int,input().split())
s = input()

tmp =s[k-1].lower()

s = s[0:k-1] + tmp + s[k:]

print(s)