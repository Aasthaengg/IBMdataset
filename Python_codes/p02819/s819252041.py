#
# 149C Next Prime
#

def isPrime(num):
    if num == 2:
        return True
    for p in range(2, num):
        if  num % p == 0:
            return False
    return True

if __name__ == "__main__":
    n = input()
    num = int(n)
    while True:
        if isPrime(num):
            print(num)
            break
        num += 1

