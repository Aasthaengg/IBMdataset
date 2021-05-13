N = int(input())
A = [int(i) for i in input().split()]

res = 0
while True:
  #check
  if len(list([i for i in A if i % 2 != 0])) == 0:
    res += 1
  else:
  	break
  #2でわる
  A = [i // 2 for i in A]

  
print(res)