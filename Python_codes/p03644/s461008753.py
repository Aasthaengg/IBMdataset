N = int(input())
l = [1,2,4,8,16,32,64][::-1]
for i in l:
  if N >= i:
    print(i)
    break