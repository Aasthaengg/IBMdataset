a, b = map(int, input().split())
 
# aの倍数を順に探索する
# abはa, bの公倍数なので、高々B回で十分。O(B)
lcm = 0
for i in range(1, b+1):
  if (a * i) % b == 0:
    lcm = a * i
    break
  
print(lcm)