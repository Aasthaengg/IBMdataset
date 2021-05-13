k = int(input())

ans = [i for i in range(50)]
cnt = k//50

for i in range(50):
  ans[i]+=cnt

amari = k%50
for i in range(50)[::-1]:
  if amari ==0:
    break
  ans[i]+=1
  amari -= 1
print(50)
print(str(ans).replace("[","").replace("]","").replace(",",""))