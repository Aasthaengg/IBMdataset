N, A, B= list(map(int, input().split()))
ans = 0
digsum = 0
for i in range(1,N+1):
  if i<10:
    digsum = i
  elif i <100:
    dig1 = i%10
    dig2 = ((i%100)-dig1)/10
    digsum = dig1 + dig2
  elif i < 1000:
    dig1 = (i%10)
    dig2 = ((i%100)-dig1)/10
    dig3 = i//100
    digsum = dig1 + dig2 + dig3
  elif i < 10000:
    dig1 = (i%10)
    dig2 = ((i%100)-dig1)/10
    dig3 = ((i%1000) - dig2*10 - dig1)/100
    dig4 = i//1000
    digsum = dig1 + dig2 + dig3 + dig4
  else:
    digsum = 1
  if (digsum>=A) and (digsum<=B):
    ans += i
print(ans)