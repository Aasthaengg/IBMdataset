n = int(input())

# nを割れる整数を1からルートnまで列挙
def divisors(num):
   arr = []
   for i in range(1, int(num**0.5) + 1):
       if num % i == 0:
           arr.append(i)
           if i != num // i:
               arr.append(num//i)
   return arr

n_div = divisors(n)
arr_ = [int(i + n / i) for i in n_div]
print(min(arr_) - 2)