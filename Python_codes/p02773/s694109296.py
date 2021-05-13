n=(int)(input())
a = sorted(list(input() for i in range(n)))
lis = sorted(list(set(a)))
big = [0 for i in range(len(lis))]
maxi = 0
counter = 1
check = 0
#print(a)
for i in range(len(a) - 1):
  #print(a[i])
  if a[i] == a[i + 1]:
    counter += 1
  else:
    big[check] = counter
    counter = 1
    check += 1
else:
  big[-1] = counter
maxi = max(big)
#print(lis, big)
for i in range(len(lis)):
  if big[i] == maxi:
    print(lis[i])