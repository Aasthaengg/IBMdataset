x=int(input())
for i in range(8):
  if i*200+400<=x and i*200+599>=x:
    print(8-i)
    break
