n, a, b = map(int, input().split())

ans = 0
for num in range(n):
  num += 1
  num_0 = num
  place_of_10000 = num//10000
  num -= 10000*place_of_10000
  place_of_1000 = num//1000
  num -= 1000*place_of_1000
  place_of_100 = num//100
  num -= 100*place_of_100
  place_of_10 = num//10
  num -= 10*place_of_10
  
  tmp = place_of_10000 + place_of_1000 + place_of_100 + place_of_10 + num
  if a<=tmp and tmp<=b:
    ans += num_0
    
print(ans)