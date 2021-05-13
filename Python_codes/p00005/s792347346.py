import sys

def dividend(num, Q):
    a = Q
    b = (num / Q) * Q
    Q = num - (num / Q) * Q
    if num  == b:
        aaa(a)
        return
    dividend(a, Q)
    
def aaa(greatest_common_divisor):
    least_common_multiple = num1 * num2 / greatest_common_divisor
    print('%s %s' % (greatest_common_divisor, least_common_multiple))
    return

for input_line in sys.stdin:
    num1 = int(input_line.split(' ')[0])
    num2 = int(input_line.split(' ')[1])
    
    if num1 <= num2:
        dividend(num2, num1)
    elif num1 > num2:
        dividend(num1, num2)