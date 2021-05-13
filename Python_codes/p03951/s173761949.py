n = int(input())
s = input()
t = input()
f = 0
m = 0
ind = 0
for i in range(1,n+1):
      if(s[n-i:]==t[:i]):
            f=1
            if (len(t[:i])>m):
                  m = len(t[:i])
                  ind = i

print(2*n-ind) if f==1 else print(2*n)
