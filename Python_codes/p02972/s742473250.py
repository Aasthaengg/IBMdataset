n = int(input())
a= list(map(int, input().split()))
s = [0]*n
ans2 = []
for i in range(1, n+1):
  temp = sum(s[n-i::n+1-i])
  if (temp % 2 == 0 and a[-i] == 1) or (temp % 2 == 1 and a[-i] == 0) :
    s[-i] = 1
    ans2.append(str(n+1-i)) 

ans2.reverse()
print(sum(s))
print(" ".join(ans2))