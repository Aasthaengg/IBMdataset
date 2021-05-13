n=int(input())
s=[int(input()) for _ in range(n)]

sum=0
for i in s:
      sum+=i

if sum%10!=0:
      print(sum)
      exit()

s.sort()
for i in s:
      if i%10!=0:
            sum-=i
            print(sum)
            exit()

print(0)

