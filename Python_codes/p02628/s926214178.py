x = input()
arr = [int(j) for j in x.split()]
y = input()
main = [int(i) for i in y.split()]
main = sorted(main)
sum = 0
r = 0
while r < arr[1]:
  sum+=main[r]
  r+=1
print(sum)