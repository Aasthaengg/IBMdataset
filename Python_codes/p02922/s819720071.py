a,b = [int(x) for x in input().split()]
sum_outlet = a
taps = 1
# A口ある電源タップを一個取り付けると、差込口はA-1個増える

if b == 1:
      print(0)
else:
      while(sum_outlet < b):
            #print(sum_outlet,taps)
            taps += 1
            sum_outlet += a-1
      print(taps)