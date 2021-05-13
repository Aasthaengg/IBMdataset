n,k=map(int,input().split())
s = input()
 
s = list(s)
s[k - 1] = s[k-1].lower()
s = "".join(s)
print(s)