n=(int)(input())
a=list(map(int, input().split(" ")))
count=0
ans=0
while(count!=len(a)):
  if a[count] % 2 == 0:
    a[count] = a[count] // 2
    ans += 1
  else:
    count += 1
print(ans)