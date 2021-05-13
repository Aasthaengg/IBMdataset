import math

def prime_detector(num):
    sqrt = int(math.sqrt(num))
    if any(num % i == 0 for i in range(2,sqrt+1)): return False
    else: return True
    
def main():

    number = int(input())
    
    numbers_tuple = tuple(int(input()) for i in range(number))
    
    print(sum(prime_detector(n) for n in numbers_tuple))

main()