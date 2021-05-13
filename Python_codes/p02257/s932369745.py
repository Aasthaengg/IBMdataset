#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C&lang=jp
#?´???°??????
#x????´???°y???2 < y < sqrt(x)??????????????¨??????

from math import sqrt,ceil

def check_prime_number(n):
    sqrt_num = ceil(sqrt(n))
    
    if n == 2:
        return True
    elif n < 2:
        return False
    elif (n % 2) == 0:
        return False
    div = 3
    while div <= sqrt_num:
        if (n % div) == 0:
            return False
        div += 2
        
    return True

def count_prime_numbers(n_list):
    ans = 0
    for n in n_list:
        if check_prime_number(n):
            ans += 1
    return ans

def main():
    num = int(input())
    target_list = [int(input()) for i in range(num)]
    print(count_prime_numbers(target_list))
    
if __name__ == "__main__":
    main()