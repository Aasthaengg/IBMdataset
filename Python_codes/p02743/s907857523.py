from decimal import Decimal
from sys import stdin
 
 
def get_result(data):
    A, B, C = data
    r_a = Decimal(A**Decimal(0.5))
    r_b = Decimal(B**Decimal(0.5))
    r_c = Decimal(C**Decimal(0.5))
    return 'Yes' if r_a + r_b < r_c else 'No'
 
 
if __name__ == '__main__':
    data = stdin.readline().rstrip().split(' ')
    data = list(map(int, data))
    result = get_result(data)
    print(result)