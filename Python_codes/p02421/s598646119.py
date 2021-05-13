n = int(input())
ts = 0
hs = 0
for i in range(n):
 taro, hanako = input().split()
 if taro > hanako:
  ts += 3
 elif taro < hanako:
  hs += 3
 else:
  ts += 1
  hs += 1
print(str(ts) + " " + str(hs))