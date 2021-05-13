h = int(input())
cnt,ex = 0,1
while h!=0:
  h = h//2
  cnt += ex
  ex *= 2
print(cnt)