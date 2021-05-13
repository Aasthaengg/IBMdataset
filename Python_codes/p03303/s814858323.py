s=input()
w=int(input())
n=-(-len(s)//w)
ans=""
for i in range(n):
  ans=ans+s[w*i]
print(ans)