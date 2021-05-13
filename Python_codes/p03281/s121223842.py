import math

def countDividers(n):
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(int(n/i))
    return len(divisors)


if __name__ == '__main__':
    n = int(input())
    count = 0
    for i in range(1,n+1):
        if i %2 ==1 and countDividers(i) == 8:
            count += 1
           
    print(count)
