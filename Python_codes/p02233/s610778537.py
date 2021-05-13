#coding:utf-8
#1_10_A
def fibo(n, numbers):
    if n == 0 or n == 1:
        numbers[n] = 1
        return numbers[n]
    elif numbers[n]:
        return numbers[n]
    else:
        numbers[n] = fibo(n - 1, numbers) + fibo(n - 2, numbers)
        return numbers[n]

n = int(input())
fibonacci_numbers = [0 for i in range(n + 1)]
print(fibo(n, fibonacci_numbers))