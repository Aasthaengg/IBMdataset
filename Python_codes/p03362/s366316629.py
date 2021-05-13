#nの素数判定
def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

N = int(input())

list = []

for i in range(55556):
    if(is_prime(i) and i % 5 == 1):
        list.append(i)
        
print(' '.join(str(item) for item in list[0:N]))