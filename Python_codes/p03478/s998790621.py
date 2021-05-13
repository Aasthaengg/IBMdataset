# 1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を求めてください。
n, a, b = [int(x) for x in input().split()]
total = 0

def digit_sum(num,digitotal = 0):
      while(num > 0):
            digitotal += num%10
            num //= 10
      return digitotal
      
for i in range(1,n+1):
      x = digit_sum(i)
      if x >= a and x <= b:
            #print(i,end=", ")
            total += i

print(total)