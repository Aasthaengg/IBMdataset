n,k=map(int,input().split())
s=list(input())
s[k-1] = chr(ord(s[k-1])-ord("A")+ord("a"))
print("".join(s))
