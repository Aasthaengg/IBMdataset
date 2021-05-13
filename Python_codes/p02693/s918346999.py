k = int(input())
list = list(map(int, input().split()))
a = list[0]
b = list[1]
for i in range(a,b+1):
  if i % k ==0:
    print("OK")
    break
  if i==b:
    print("NG")