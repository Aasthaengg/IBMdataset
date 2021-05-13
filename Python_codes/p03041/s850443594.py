#include<bits/stdc++.h>
n,k=map(int,input().split())
s=input()
c=""
for i in range(n):
  if i==k-1:
    c+=s[i].lower()
  else:
    c+=s[i]
print(c);