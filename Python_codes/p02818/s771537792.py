a,b,k = map(int,input().split())
taka = a
aoki = b
recur = k
if taka>=k:
  print("{} {}".format(taka-k,aoki))
elif k>=taka and (aoki+taka)>=k:
  print("{} {}".format(0,aoki-(k-taka)))
elif (aoki+ taka)<=k:
  print("0 0")

