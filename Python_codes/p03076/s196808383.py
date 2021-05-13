a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
ans = 0
l = [a,b,c,d,e]
ld = [(a+9)%10,(b+9)%10,(c+9)%10,(d+9)%10,(e+9)%10]
i = ld.index(min(ld))
last = l[i]
l.remove(l[i])
for j in l:
  ans += ((j+9)//10)*10
print(ans+last)