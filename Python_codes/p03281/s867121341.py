#約数
def make_divisors(n): #約数をリストで返す
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

# 初期入力
import sys
input = sys.stdin.readline  #文字列では使わない
N = int(input())

count =0
for i in range(1,N+1,2):
    x =make_divisors(i)
    if len(x) ==8:
        count +=1
print(count)