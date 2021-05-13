n=int(input())
s=input()
print('YNeos'[(n%2!=0 or s[0:n//2]!=s[n//2:n])::2])