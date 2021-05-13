n   = int(input())
li  = list(map(int,input().split()))
cnt = 0

for i in range(n-2):
  li2 = []
  li2.append(li[i])
  li2.append(li[i+1])
  li2.append(li[i+2])
  li2.sort()
  if li2[1] == li[i+1]:
    cnt += 1

print(cnt)