n=int(input())
a=sorted(list(map(int, input().split(" "))))
if sum(a) == 0:
  print("Yes")
elif n % 3 != 0:
  print("No")
else:
  ass = [a[0], a[n // 3], a[n // 3 * 2]]
  #print(a.count(ass[0]), (n // 3))
  if a.count(ass[0]) % (n // 3) != 0 or a.count(ass[1]) % (n // 3) != 0 or a.count(ass[2]) % (n // 3) != 0:
    print("No")
  else:
    if ass[0] ^ ass[1] != ass[2]:
      print("No")
    else:
      print("Yes")