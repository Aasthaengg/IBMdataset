n,c,k = map(int ,input().split(" "))
t = sorted([int(input()) for i in range(n)])
total = 0
count = 0
while(count != n):
  temp = 0
  #print(count, total)
  for i in range(c):
    if count + i >= n:
      #print("乗りたい人数を全部さばいた")
      if t[-1] - t[count] <= k:
        #print("最後の人全員載せる")
        count = n
        total += 1
        break
      else:
        temp = 0
        while(count != n):
          #print("残りを何回で載せられるか")
          if t[count + temp] - t[count] <= k:
            temp += 1
          else:
            count += temp + 1
            total += 1
        break
      break
    if t[count + i] - t[count] > k:
      #print("定員を超えた")
      count += i
      total += 1
      break
  else:
    #print("k人全員載せる")
    count += c
    total += 1
    if count == n:
      break
print(total)