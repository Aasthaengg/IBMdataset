X = int(input())
ppap = 0
# for i in range(100 , L):
a = 100
while a < X:
  a += a//100
  ppap += 1
print(ppap)